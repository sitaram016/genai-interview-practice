import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    # Load environment variables from .env
    load_dotenv()

    # Create OpenAI client using API key
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Simple GenAI inference
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Explain Generative AI in one simple sentence."
    )

    # Print model output
    print(response.output_text)

if __name__ == "__main__":
    main()
