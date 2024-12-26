import httpx
import json
from typing import Dict, Any


async def post(
    api_key: str,
    messages: list[Dict[str, str]],
    model: str = "openai/gpt-3.5-turbo"
) -> Dict[str, Any]:
    """
    Send a request to OpenRouter API using httpx

    Args:
        api_key: OpenRouter API key
        messages: List of message objects
        model: Model to use (default: gpt-3.5-turbo)

    Returns:
        API response as dictionary
    """

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()

# Example usage:
"""
messages = [
    {
        "role": "user",
        "content": "What is the meaning of life?"
    }
]

response = await send_openrouter_request(
    api_key=OPENROUTER_API_KEY,
    messages=messages
)
"""
