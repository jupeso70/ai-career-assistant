# AI Career Assistant

An AI-powered job application assistant that analyzes how well a candidate's CV matches a job description and generates tailored application materials.

This project is designed as a practical first AI-agent project using Python, PDF parsing, and the OpenAI API.

## Features

- Read CV text directly from a PDF file
- Read job description from a text file
- Analyze CV-to-job match
- Generate a match score
- Identify strengths and missing skills
- Suggest CV improvements
- Generate a tailored cover letter draft
- Export results as Markdown files

## Technology Stack

- Python 3.12+
- OpenAI API
- PyPDF
- python-dotenv
- Markdown reports

## Project Structure

```text
ai-career-assistant/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── cv/
│   └── cv.pdf
│
├── jobs/
│   └── job_ad.txt
│
├── reports/
│
└── src/
    ├── main.py
    ├── pdf_reader.py
    ├── openai_client.py
    ├── analyzer.py
    └── report_generator.py
```

## Installation

Clone or download the project.

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment on Windows:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\activate
```

Activate environment on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## OpenAI API Setup

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Edit `.env` and add your API key:

```text
OPENAI_API_KEY=your_api_key_here
```

## Usage

Place your CV here:

```text
cv/cv.pdf
```

Place the job advertisement here:

```text
jobs/job_ad.txt
```

Run the application:

```bash
python src/main.py
```

Generated files will appear in:

```text
reports/
├── match_report.md
└── cover_letter.md
```

## Example Output

```text
Match Score: 87/100

Strengths:
- Automotive software integration
- AUTOSAR Classic
- CI/CD
- Radar systems

Missing Skills:
- Kubernetes
- Helm
- Cloud technologies
```

## Future Improvements

- GUI
- Multiple CV versions
- LinkedIn profile analysis
- Automatic job scraping
- n8n workflow integration
- PDF report generation
- DOCX cover letter generation
- Application tracking database

## License

MIT License
