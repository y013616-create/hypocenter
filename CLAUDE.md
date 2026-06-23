# CLAUDE.md

## Project Overview

Automation pipeline that converts PDF academic papers to Markdown and generates LLM Wiki entries for each keyword using the Claude API.

## Language & Framework

- **Language**: Python 3.11+
- **AI**: Anthropic Claude API (`claude-opus-4-8`, adaptive thinking, streaming)
- **PDF conversion**: `pymupdf4llm`
- **CLI**: `click`

## Project Structure

```
hypocenter/
├── src/
│   ├── pdf_converter.py      # PDF → Markdown via pymupdf4llm
│   ├── keyword_extractor.py  # Claude API keyword extraction
│   ├── wiki_generator.py     # Claude API wiki entry generation
│   └── pipeline.py           # Orchestrates the full pipeline
├── scripts/
│   └── process_paper.py      # CLI entry point
├── output/
│   ├── papers/               # Converted Markdown papers
│   └── wiki/                 # Per-paper wiki directories
│       └── <paper_stem>/
│           └── <keyword>.md
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-...
```

## Usage

```bash
# Basic usage
python scripts/process_paper.py path/to/paper.pdf

# Custom output directory and keyword limit
python scripts/process_paper.py paper.pdf --output-dir ./results --max-keywords 15

# Quiet mode (machine-readable output)
python scripts/process_paper.py paper.pdf --quiet
```

## Pipeline Steps

1. **PDF → Markdown**: `pymupdf4llm` extracts structured text preserving headings, tables, and formatting.
2. **Keyword extraction**: Claude reads the full Markdown and returns a ranked JSON list of technical keywords.
3. **Wiki generation**: For each keyword, Claude produces a structured Markdown wiki entry with sections: Definition, Context in Paper, Related Concepts, Key Properties, Examples, References.

## Architecture Notes

- A single `anthropic.Anthropic()` client is reused across all API calls in a pipeline run.
- All Claude calls use `thinking: {type: "adaptive"}` and streaming (`.stream()` + `.get_final_message()`).
- Wiki files are named `<keyword_with_underscores>.md` inside `output/wiki/<paper_stem>/`.
