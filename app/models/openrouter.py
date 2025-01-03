from app.logger import logger
from app.utils import get_key
from app.prompt import BASE_PROMPT
import httpx
import json
from typing import Dict, Any, AsyncGenerator


async def stream(
    api_key: str,
    messages: list[Dict[str, str]],
    model: str = "openai/gpt-3.5-turbo"
) -> AsyncGenerator[str, None]:
    """
    Stream responses from OpenRouter API

    Args:
        api_key: OpenRouter API key
        messages: List of message objects
        model: Model to use

    Yields:
        Streamed response content
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages,
        "stream": True  # Enable streaming
    }

    async with httpx.AsyncClient() as client:
        async with client.stream(
            "POST",
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30.0
        ) as response:
            response.raise_for_status()

            async for line in response.aiter_lines():
                if line.strip():  # Skip empty lines
                    if line.startswith("data: "):
                        line = line[6:]  # Remove "data: " prefix
                    if line != "[DONE]":
                        try:
                            chunk = json.loads(line)
                            if content := chunk.get("choices", [{}])[0].get("delta", {}).get("content"):
                                yield content
                        except json.JSONDecodeError:
                            continue


async def answer(query: str, prompt: str = BASE_PROMPT, model: str = "deepseek/deepseek-chat") -> AsyncGenerator[str, None]:
    try:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ]
        async for chunk in stream(
            api_key=get_key("OPENROUTER_API_KEY"),
            messages=messages,
            model=model
        ):
            yield chunk
    except Exception as e:
        logger.error(f"Error in deepseek: {str(e)}")
        yield "[ERROR] Failed to get response from API"
