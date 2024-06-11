# async_requests.py

import asyncio
import aiohttp

async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['http://localhost:5000/home'] * 10000
    tasks = [make_request(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    return responses

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    # Process results to count requests handled by each server instance and visualize in a bar chart
    # Print or save the counts for analysis
