from pathlib import Path


def save_markdown_report(content: str, output_path: str | Path) -> None:
    """Save Markdown content to a file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
