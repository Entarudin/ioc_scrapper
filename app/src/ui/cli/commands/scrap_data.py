from app.src.container import container
from app.src.ui.cli.commands.base_command import BaseCommand


class ScrapDataCommand(BaseCommand):
    async def _execute(self):
        await container.scrapper_service.start_scrapping()
