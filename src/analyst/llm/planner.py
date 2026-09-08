import json

from analyst.llm.client import client
from analyst.llm.tools import TOOLS
from analyst.core.config import settings

SYSTEM = (
    "You are a data analyst. Use the available tools to answer questions "
    "about a dataset. Only use column names that appear in the provided "
    "dataset profile — never invent column names."
)

def plan(question: str, profile: dict) -> dict:
    response = client.chat.completions.create(
        model=settings.groq_model,
        messages=[
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": f"Dataset profile:\n{json.dumps(profile)}\n\nQuestion: {question}"},
],
        tools=TOOLS,
    )


    tool_calls = response.choices[0].message.tool_calls

    if not tool_calls:
        raise ValueError("Could not map that question to an available analysis")

    call = tool_calls[0]

    return {
        "function": call.function.name,
        "arguments": json.loads(call.function.arguments),
    }