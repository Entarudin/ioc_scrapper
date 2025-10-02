from app.src.ui.cli.commands import ScrapDataCommand
import asyncio


async def main() -> None:
    command = ScrapDataCommand()
    await command.execute()


if __name__ == "__main__":
    asyncio.run(main())
