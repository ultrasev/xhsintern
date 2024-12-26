from typing import AsyncGenerator
from .openrouter import stream
from app.utils import get_key
from app.logger import logger
from app.prompt import BASE_PROMPT


async def deepseek(query: str, prompt: str = BASE_PROMPT) -> AsyncGenerator[str, None]:
    try:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ]
        async for chunk in stream(
            api_key=get_key("OPENROUTER_API_KEY"),
            messages=messages,
            model="deepseek/deepseek-chat"
        ):
            yield chunk
    except Exception as e:
        logger.error(f"Error in deepseek: {str(e)}")
        yield "[ERROR] Failed to get response from API"
