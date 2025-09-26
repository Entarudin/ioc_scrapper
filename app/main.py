import asyncio

from src import container


async def main():
    virus_total_base_url = container.scrapper_config.get_scrapper_virus_total_base_url()
    scrapper_factory = container.get_scrappers_factory

    virus_total_scraper = scrapper_factory.create(virus_total_base_url)
    virus_total_info = await virus_total_scraper.scrape("8.8.8.8")
    print(virus_total_info)


if __name__ == "__main__":
    asyncio.run(main())
