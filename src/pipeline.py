import anthropic
from pathlib import Path

from .pdf_converter import convert_pdf_to_markdown, save_markdown
from .keyword_extractor import extract_keywords
from .wiki_generator import generate_wiki_entry, save_wiki_entry, generate_index_note


def run_pipeline(
    pdf_path: str | Path,
    output_dir: str | Path = "output",
    max_keywords: int = 20,
    verbose: bool = True,
) -> dict:
    """
    Full pipeline: PDF → Markdown → keyword extraction → Obsidian wiki entries.

    Returns a dict with paths to all generated files.
    """
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    client = anthropic.Anthropic()

    papers_dir = output_dir / "papers"
    wiki_dir = output_dir / "wiki" / pdf_path.stem

    # Step 1: Convert PDF to Markdown
    if verbose:
        print(f"[1/3] Converting PDF to Markdown: {pdf_path.name}")
    md_text = convert_pdf_to_markdown(pdf_path)
    md_path = save_markdown(md_text, papers_dir / f"{pdf_path.stem}.md")
    if verbose:
        print(f"      Saved → {md_path}")

    # Step 2: Extract keywords
    if verbose:
        print("[2/3] Extracting keywords...")
    keywords = extract_keywords(md_text, client=client)
    keywords = keywords[:max_keywords]
    if verbose:
        print(f"      Found {len(keywords)} keywords: {', '.join(keywords)}")

    # Step 3: Generate wiki entries (Obsidian-compatible)
    if verbose:
        print(f"[3/3] Generating Obsidian wiki entries for {len(keywords)} keywords...")
    wiki_paths = []
    for i, keyword in enumerate(keywords, 1):
        if verbose:
            print(f"      [{i}/{len(keywords)}] {keyword}")
        wiki_text = generate_wiki_entry(
            keyword=keyword,
            md_text=md_text,
            paper_stem=pdf_path.stem,
            all_keywords=keywords,
            client=client,
        )
        wiki_path = save_wiki_entry(keyword, wiki_text, wiki_dir)
        wiki_paths.append(wiki_path)

    # Step 4: Generate Obsidian index (MOC) note
    index_path = generate_index_note(pdf_path.stem, keywords, wiki_dir)
    if verbose:
        print(f"\nDone!")
        print(f"  Wiki entries : {wiki_dir}/")
        print(f"  Index note   : {index_path}")
        print(f"\nObsidian vault tip: point your vault at '{output_dir}/' to use wikilinks.")

    return {
        "pdf": pdf_path,
        "markdown": md_path,
        "keywords": keywords,
        "wiki_dir": wiki_dir,
        "wiki_files": wiki_paths,
        "index": index_path,
    }
