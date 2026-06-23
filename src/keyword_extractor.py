import anthropic


SYSTEM_PROMPT = """\
You are an expert academic research assistant. Your task is to extract the most important \
technical keywords and concepts from a research paper provided in Markdown format.

Return ONLY a JSON array of keyword strings. Each keyword should be:
- A specific technical term, concept, method, model, or dataset name
- Meaningful on its own (not vague words like "approach" or "result")
- Between 1 and 5 words
- Ordered by importance/frequency in the paper

Example output:
["transformer", "attention mechanism", "BERT", "fine-tuning", "named entity recognition"]
"""


def extract_keywords(md_text: str, client: anthropic.Anthropic | None = None) -> list[str]:
    if client is None:
        client = anthropic.Anthropic()

    prompt = f"Extract the key technical keywords from this research paper:\n\n{md_text}"

    with client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=1024,
        thinking={"type": "adaptive"},
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        response = stream.get_final_message()

    # Find the text block in the response
    raw = ""
    for block in response.content:
        if block.type == "text":
            raw = block.text
            break

    # Parse JSON array from response
    import json
    import re

    match = re.search(r"\[.*?\]", raw, re.DOTALL)
    if not match:
        raise ValueError(f"Could not parse keyword list from response:\n{raw}")

    keywords = json.loads(match.group())
    return [str(k) for k in keywords]
