import asyncio
import time
import aiohttp
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient('localhost', 27017)
db = client['fun']
collection = db['hp']


async def get_data(page):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Origin": "https://1019135.tgsph1.xyz",
        "Pragma": "no-cache",
        "Referer": "https://1019135.tgsph1.xyz/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47",
        "sec-ch-ua": "^\\^Chromium^^;v=^\\^106^^, ^\\^Microsoft",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^"
    }
    url = "https://api.tgspa5.xyz/v1/videos"
    params = {
        "category": "1",
        "tags": "",
        "order_by": "updated_at",
        "per_page": "20",
        "page": page
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, params=params) as resp:
            dic = await resp.json()
            movies = dic['data']['items']
            for movie in movies:
                title = movie['title']
                url_movie = 'https://1019135.tgsph1.xyz/#/play/' + str(movie['id'])
                views = movie['views']
                content = {'Title': title, 'URL': url_movie, 'Views': views}
                await save_data(content)


async def save_data(data):
    if data:
        return await collection.insert_one(data)


async def run():
    task_list = []
    for i in range(200):
        res = get_data(i)
        task = asyncio.create_task(res)
        task_list.append(task)
    await asyncio.wait(task_list)


if __name__ == '__main__':
    s = time.time()
    asyncio.run(run())
    print(time.time() - s)
