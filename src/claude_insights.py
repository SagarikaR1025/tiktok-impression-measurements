import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def generate_creator_insights(summary_text):

    prompt = f"""
    You are a data analyst helping interpret TikTok creator performance data.

    Based on the following analytics summary, generate:
    1. Three key insights
    2. Three creator strategy recommendations
    3. One short executive summary

    Analytics summary:
    {summary_text}
    """

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=700,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.content[0].text