import anthropic
from pathlib import Path


SYSTEM_PROMPT = """\
You are an expert technical writer creating an LLM Wiki — a structured knowledge base of \
AI/ML and academic concepts. Given a keyword and the research paper context (in Markdown), \
produce a comprehensive wiki entry in Markdown format.

The wiki entry must follow this exact structure:

# {keyword}

## Definition
A clear, concise definition of the concept.

## Context in Paper
How this concept is used, discussed, or contributed to in the specific paper.

## Related Concepts
A bullet list of related terms and how they connect to this keyword.

## Key Properties / Characteristics
Important properties, formulas, or characteristics of this concept.

## Examples
Concrete examples or instantiations of this concept (from the paper or in general).

## References
- The paper being analyzed (with title and authors if available)
- Any other works cited in relation to this concept

Write in clear, precise technical language. Use LaTeX math notation ($...$ or $$...$$) \
where appropriate. Be specific and avoid vague generalizations.
"""


def generate_wiki_entry(
    keyword: str,
    md_text: str,
    client: anthropic.Anthropic | None = None,
) -> str:
    if client is None:
        client = anthropic.Anthropic()

    prompt = (
        f"Generate a wiki entry for the keyword: **{keyword}**\n\n"
        f"Here is the research paper for context:\n\n{md_text}"
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
    safe_name = keyword.replace(" ", "_").replace("/", "-").lower()
    output_path = output_dir / f"{safe_name}.md"
    output_path.write_text(wiki_text, encoding="utf-8")
    return output_path
