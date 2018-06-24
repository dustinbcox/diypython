#!/usr/bin/env python3
"""Web scraper (asyncio version).
This was a code sample requested by Ayan who gave a talk at Orlando Devs on June 2018"""

# pip install aiohttp
# pip install beautifulsoup4

import aiohttp
import asyncio

from bs4 import BeautifulSoup


async def fetch_titles(*urls):
    """fetch html title from url(s)"""
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        return await asyncio.gather(*[fetch_title(session, url) for url in urls])

async def fetch_title(session, url):
    """Request the url (using aiohttp session) and return html title"""
    async with session.get(url) as response:
        # TODO check response.status == 200:
        return BeautifulSoup(await response.text(), 'html.parser').title.string


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(
        fetch_titles("https://www.google.com/",
        "https://www.reddit.com/",
        "https://digg.com/"))
    loop.run_until_complete(future)
    titles = future.result()
    print(titles)
