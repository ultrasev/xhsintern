from typing import AsyncGenerator
from .openrouter import answer
from app.prompt import BASE_PROMPT


async def deepseek(query: str,
                   prompt: str = BASE_PROMPT) -> AsyncGenerator[str, None]:
    async for chunk in answer(query, prompt):
        yield chunk
