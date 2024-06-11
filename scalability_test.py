# scalability_test.py

import asyncio
import aiohttp

async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main(N):
    urls = ['http://localhost:5000/home'] * 10000
    tasks = [make_request(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    # Process responses to calculate average load
    return avg_load

if __name__ == "__main__":
    for N in range(2, 7):
        avg_load = asyncio.run(main(N))
        # Print or save avg_load for each value of N
