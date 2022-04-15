import trio

import ddg_scraper

scraper = ddg_scraper.DuckScraper()


async def main():
    # with scraper.search("python") as results:
    #     for result in results:
    #         print(result.title)

    async with scraper.search("python") as results:
        async for result in results:
            print(result.title)
            print(result.url)


if __name__ == "__main__":
    trio.run(main)
