import asyncio
from app.models.deepseek import deepseek
from app.prompt import STARSEEKER


async def main():
    with open("/tmp/x.txt", "r") as f:
        content = f.read()
    async for chunk in deepseek(content, STARSEEKER):
        print(chunk, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
