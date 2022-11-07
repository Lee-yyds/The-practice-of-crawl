# File       : stream.py
# Time       ：2022/11/6 12:09
# Author     ：LyChow
# version    ：python 3.10.8
import requests

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Origin": "https://bulletin.cebpubservice.com",
    "Referer": "https://bulletin.cebpubservice.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^"
}
url = "https://details.cebpubservice.com:7443/bulletin/getBulletin/8a94948283ef5a5101844b20cfaa54ad"
response = requests.get(url, headers=headers, stream=True)
with open('1.pdf', 'wb') as f:
    for i in response.iter_content(chunk_size=512):
        if i:
            f.write(i)
