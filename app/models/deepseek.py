from typing import Optional
from .openrouter import post

from utils import get_key


async def deepseek(query: str, prompt: str) -> Optional[str]:
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
        print(f"Error in deepseek: {str(e)}")
        return None
