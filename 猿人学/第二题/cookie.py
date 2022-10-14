import requests

headers = {
    "authority": "match.yuanrenxue.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.com/match/2",
    "sec-ch-ua": "^\\^Chromium^^;v=^\\^106^^, ^\\^Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "m": "326d905df12e29e83b134dadb5ac3a39^|1665460878000"
}
url = "https://match.yuanrenxue.com/api/loginInfo"
response = requests.get(url, headers=headers, cookies=cookies)
print(response.cookies)
# print(response.text)
# print(response)
