import pymupdf4llm
from pathlib import Path


def convert_pdf_to_markdown(pdf_path: str | Path) -> str:
    """Convert a PDF file to Markdown using pymupdf4llm."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a .pdf file, got: {pdf_path.suffix}")

    md_text = pymupdf4llm.to_markdown(str(pdf_path))
    return md_text


def save_markdown(md_text: str, output_path: str | Path) -> Path:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md_text, encoding="utf-8")
    return output_path
