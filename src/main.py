from pathlib import Path

from analyzer import analyze_cv_match, generate_cover_letter
from openai_client import create_openai_client
from pdf_reader import read_pdf_text
from report_generator import save_markdown_report


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CV_PATH = PROJECT_ROOT / "cv" / "cv.pdf"
JOB_AD_PATH = PROJECT_ROOT / "jobs" / "job_ad.txt"
REPORTS_DIR = PROJECT_ROOT / "reports"


def read_job_ad(path: Path) -> str:
    """Read job advertisement text from file."""
    if not path.exists():
        raise FileNotFoundError(f"Job advertisement file not found: {path}")

    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError(f"Job advertisement file is empty: {path}")

    return text


def main() -> None:
    print("AI Career Assistant")
    print("===================")

    print(f"Reading CV: {CV_PATH}")
    cv_text = read_pdf_text(CV_PATH)

    print(f"Reading job advertisement: {JOB_AD_PATH}")
    job_text = read_job_ad(JOB_AD_PATH)

    print("Creating OpenAI client...")
    client = create_openai_client()

    print("Analyzing CV match...")
    match_report = analyze_cv_match(client, cv_text, job_text)
    save_markdown_report(match_report, REPORTS_DIR / "match_report.md")

    print("Generating cover letter...")
    cover_letter = generate_cover_letter(client, cv_text, job_text)
    save_markdown_report(cover_letter, REPORTS_DIR / "cover_letter.md")

    print("\nDone.")
    print(f"Match report: {REPORTS_DIR / 'match_report.md'}")
    print(f"Cover letter: {REPORTS_DIR / 'cover_letter.md'}")


if __name__ == "__main__":
    main()
