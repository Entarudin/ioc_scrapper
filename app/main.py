import asyncio

from src import container


async def main():
    logger = container.app_logger


if __name__ == "__main__":
    asyncio.run(main())
