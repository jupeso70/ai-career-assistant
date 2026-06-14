import os
from dotenv import load_dotenv
from openai import OpenAI


def create_openai_client() -> OpenAI:
    """Create an OpenAI client using OPENAI_API_KEY from environment variables."""
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY is missing. Create a .env file based on .env.example."
        )

    return OpenAI(api_key=api_key)
