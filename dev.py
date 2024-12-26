
import asyncio
from app.models.deepseek import deepseek


async def main():
    print(await deepseek("你好"))

if __name__ == "__main__":
    asyncio.run(main())
