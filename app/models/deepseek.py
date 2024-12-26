from typing import Optional
from .openrouter import post

from app.utils import get_key
from app.logger import logger
from app.prompt import BASE_PROMPT


async def deepseek(query: str, prompt: str = BASE_PROMPT) -> Optional[str]:
    try:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ]
        response = await post(
            api_key=get_key("OPENROUTER_API_KEY"),
            messages=messages,
            model="deepseek/deepseek-chat"
        )

        return response.get("choices", [{}])[0].get("message", {}).get("content")
    except Exception as e:
        logger.error(f"Error in deepseek: {str(e)}")
        return None
