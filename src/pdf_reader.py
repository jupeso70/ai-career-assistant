from pathlib import Path
from pypdf import PdfReader


def read_pdf_text(pdf_path: str | Path) -> str:
    """Read text content from a PDF file."""
    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    reader = PdfReader(str(path))
    text_parts: list[str] = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        text_parts.append(f"\n--- Page {page_number} ---\n{page_text}")

    text = "\n".join(text_parts).strip()

    if not text:
        raise ValueError(
            "No text could be extracted from the PDF. "
            "The file may be scanned or image-based."
        )

    return text
