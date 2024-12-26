from app.models.openrouter import answer
from app.prompt import BASE_PROMPT
from typing import AsyncGenerator

MODELS = [
    'deepseek/deepseek-chat',
    'openai/gpt-4o-mini',
    'google/gemini-pro-1.5',
    'qwen/qwen-2.5-72b-instruct'
]

CUTTING_LINE = "----------------------------------------"


async def multiple(query: str, prompt: str = BASE_PROMPT) -> AsyncGenerator[str, None]:
    for model in MODELS:
        print(f"{CUTTING_LINE} {model} {CUTTING_LINE}")
        async for chunk in answer(query, prompt, model):
            yield chunk
        yield "\n\n"
