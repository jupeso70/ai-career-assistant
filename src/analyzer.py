from openai import OpenAI


DEFAULT_MODEL = "gpt-4.1-mini"


def analyze_cv_match(client: OpenAI, cv_text: str, job_text: str, model: str = DEFAULT_MODEL) -> str:
    """Analyze how well a CV matches a job advertisement."""
    prompt = f"""
You are an expert career assistant and technical recruiter.

Analyze how well the candidate CV matches the job advertisement.

Focus especially on:
- software integration
- embedded systems
- system testing
- verification and validation
- CI/CD
- tools and technologies
- domain experience
- missing keywords

Return the answer in Markdown format with these sections:

# CV Match Report

## Match Score
Give a score from 0 to 100 and explain briefly.

## Strong Matches
List the strongest matches between the CV and the job advertisement.

## Missing or Weak Areas
List missing, weak, or unclear areas.

## Transferable Skills
Identify experience from the candidate's background that can transfer successfully into this role.

Use this format:

- Current experience: ...
  Transferable to: ...
  Why it matters: ...

Focus especially on mapping:
- automotive radar experience to sensor systems
- embedded software integration to platform/system integration
- CI/CD and release management to continuous delivery
- system testing cooperation to verification and validation
- international customer deliveries to stakeholder collaboration

## Suggested CV Improvements
Suggest concrete wording or keyword improvements.

## Application Strategy
Explain how the candidate should position themselves for this role.

CV:
{cv_text}

Job Advertisement:
{job_text}
"""

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text


def generate_cover_letter(client: OpenAI, cv_text: str, job_text: str, model: str = DEFAULT_MODEL) -> str:
    """Generate a tailored cover letter draft."""
    prompt = f"""
You are an expert career assistant.

Write a concise and professional cover letter in English for the job advertisement below.

The candidate has a strong background in:
- software integration
- automotive embedded systems
- radar software platforms
- CI/CD
- C/C++ and Python
- AUTOSAR Classic
- system testing cooperation
- release and delivery coordination

Guidelines:
- Keep it professional and natural.
- Do not exaggerate.
- Do not invent experience not supported by the CV.
- Keep it around 250-350 words.
- Emphasize relevant strengths from the CV.

CV:
{cv_text}

Job Advertisement:
{job_text}
"""

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text
