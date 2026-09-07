from analyst.core.config import settings

from groq import Groq

client = Groq(api_key = settings.groq_api_key)

def complete(prompt: str) -> str:
    

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=settings.groq_model,
    )

    return chat_completion.choices[0].message.content