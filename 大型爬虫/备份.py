import time
import pymongo
import requests
from concurrent.futures.thread import ThreadPoolExecutor
import aiohttp
import asyncio


async def get_data(page):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://zxts.zjzwfw.gov.cn",
        "Pragma": "no-cache",
        "Referer": "https://zxts.zjzwfw.gov.cn/zwmhww/index.html",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42",

    }
    cookies = {
        "sessionId": "vokwlBXv7kMLbvcIPP6FfIBo0jaVHxik",
        "zh_choose_undefined": "s"
    }
    url = "https://zxts.zjzwfw.gov.cn/service/api/xfpt/public/list"
    data = {"pageSize": 10, "pageNum": page, "bt": "", "bldw": "", "startTime": "", "endTime": "", "wtsdxzqhdm": "",
            "xfmd": "", "xfxs": "", "code": "33"}
    # print(data)
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, headers=headers, cookies=cookies, data=data) as response:
            print(f'{page}页采集完毕')
    #         await asyncio.sleep(1)
            page_text = await response.text()
            print(page_text)
        return page_text


async def main():
    task_list = []
    for i in range(1,50):
        res = get_data(i)
        task = asyncio.create_task(res)
        task_list.append(task)
        # print(res)
    await asyncio.wait(task_list)

if __name__ == '__main__':
    s = time.time()
    # 9.907257795333862
    # client = pymongo.MongoClient(host='localhost', port=27017)
    # # db = client.test2
    # with ThreadPoolExecutor(10) as f:
    #     for i in range(1, 30):
    #         f.submit(main, i)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # asyncio.run(main())

    print(time.time() - s)