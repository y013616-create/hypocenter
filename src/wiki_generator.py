import anthropic
from datetime import date
from pathlib import Path


SYSTEM_PROMPT = """\
You are an expert technical writer creating an LLM Wiki — a structured knowledge base of \
AI/ML and academic concepts optimized for Obsidian.

Given a keyword, its paper source, a list of all other keywords from the same paper, \
and the full paper in Markdown, produce a wiki entry in Markdown format.

The entry MUST start with YAML frontmatter followed by the body:

---
tags: [wiki, <one or two short lowercase topic tags relevant to the keyword>]
aliases: [<common abbreviation or alternative name if any, else omit this line>]
paper: "[[<paper_stem>]]"
created: <today_date>
---

# {keyword}

## Definition
A clear, concise definition of the concept.

## Context in Paper
How this concept is used, discussed, or contributed to in the specific paper.

## Related Concepts
A bullet list. For every related concept that appears in the provided keyword list, \
use Obsidian wikilink syntax: `- [[keyword_file_name]] — brief explanation`. \
For concepts NOT in the list, write plain text.

## Key Properties / Characteristics
Important properties, formulas, or characteristics. Use LaTeX ($...$ or $$...$$) where appropriate.

## Examples
Concrete examples from the paper or in general.

## References
- [[<paper_stem>]] — source paper
- Any other cited works relevant to this concept

Rules:
- Wikilinks use the file name format: lowercase, spaces replaced by underscores (e.g. [[attention_mechanism]])
- Do not invent wikilinks for concepts not in the keyword list
- Be specific and avoid vague generalizations
"""


def _keyword_to_filename(keyword: str) -> str:
    return keyword.replace(" ", "_").replace("/", "-").lower()


def generate_wiki_entry(
    keyword: str,
    md_text: str,
    paper_stem: str,
    all_keywords: list[str],
    client: anthropic.Anthropic | None = None,
) -> str:
    if client is None:
        client = anthropic.Anthropic()

    other_keywords = [k for k in all_keywords if k != keyword]
    keyword_list_str = ", ".join(
        f"{k} → [[{_keyword_to_filename(k)}]]" for k in other_keywords
    )

    prompt = (
        f"Generate a wiki entry for the keyword: **{keyword}**\n\n"
        f"Paper file name (for wikilinks): {paper_stem}\n"
        f"Today's date: {date.today().isoformat()}\n"
        f"Other keywords from the same paper (use wikilinks for these): {keyword_list_str}\n\n"
        f"Full paper:\n\n{md_text}"
    )

    with client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=4096,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        response = stream.get_final_message()

    wiki_text = ""
    for block in response.content:
        if block.type == "text":
            wiki_text = block.text
            break

    return wiki_text


def save_wiki_entry(keyword: str, wiki_text: str, output_dir: str | Path) -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_name = _keyword_to_filename(keyword)
    output_path = output_dir / f"{safe_name}.md"
    output_path.write_text(wiki_text, encoding="utf-8")
    return output_path


def generate_index_note(
    paper_stem: str,
    keywords: list[str],
    output_dir: str | Path,
) -> Path:
    """Generate an Obsidian MOC (Map of Content) index note for the paper."""
    output_dir = Path(output_dir)
    today = date.today().isoformat()

    lines = [
        "---",
        f'tags: [paper-index]',
        f"created: {today}",
        "---",
        "",
        f"# {paper_stem}",
        "",
        f"> Source paper: [[papers/{paper_stem}]]",
        "",
        "## Keywords",
        "",
    ]
    for kw in keywords:
        fname = _keyword_to_filename(kw)
        lines.append(f"- [[{fname}|{kw}]]")

    index_path = output_dir / "_index.md"
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return index_path
