from openai import OpenAI

from app.config.settings import settings


client = OpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def ask_ai(user_message: str) -> str:

    response = client.chat.completions.create(

        model="qwen/qwen3-30b-a3b",

        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente virtual profissional, educado e objetivo. "
                    "Responda sempre em português do Brasil."
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response.choices[0].message.content