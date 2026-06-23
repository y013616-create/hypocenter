#!/usr/bin/env python3
"""CLI entry point for the PDF → Markdown → LLM Wiki pipeline."""
import sys
from pathlib import Path

import click

# Allow running as `python scripts/process_paper.py` without installing the package
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.pipeline import run_pipeline


@click.command()
@click.argument("pdf_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--output-dir",
    "-o",
    default="output",
    show_default=True,
    type=click.Path(path_type=Path),
    help="Directory where papers/ and wiki/ subdirectories will be created.",
)
@click.option(
    "--max-keywords",
    "-k",
    default=20,
    show_default=True,
    type=int,
    help="Maximum number of keywords to generate wiki entries for.",
)
@click.option("--quiet", "-q", is_flag=True, help="Suppress progress output.")
def main(pdf_path: Path, output_dir: Path, max_keywords: int, quiet: bool) -> None:
    """Convert a PDF paper to Markdown and generate LLM wiki entries per keyword."""
    result = run_pipeline(
        pdf_path=pdf_path,
        output_dir=output_dir,
        max_keywords=max_keywords,
        verbose=not quiet,
    )

    if quiet:
        # Print machine-readable summary
        print(f"markdown:{result['markdown']}")
        print(f"wiki_dir:{result['wiki_dir']}")
        for kw in result["keywords"]:
            print(f"keyword:{kw}")


if __name__ == "__main__":
    main()
