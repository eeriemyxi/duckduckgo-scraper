from ddg_scraper import search, asearch
import asyncio

# for i in search('hello'):
#     print(i)

async def main():
    async for i in await asearch("hello"):
        print(i)


asyncio.run(main())
