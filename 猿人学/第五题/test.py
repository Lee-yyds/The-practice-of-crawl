import time
import requests
import execjs

with open('cookie.js') as f:
    js = f.read()
RM4hZBv0dDon443M = execjs.compile(js).call('get_cookie')
m = execjs.compile(js).call('get_m')
print(RM4hZBv0dDon443M)
print(m)
headers = {
    "authority": "match.yuanrenxue.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.com/match/5",
    "sec-ch-ua": '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "sessionid": "oxwma18hpoqwe4kl9bsdtksn9te30n73",
    "RM4hZBv0dDon443M": RM4hZBv0dDon443M}
url = "https://match.yuanrenxue.com/api/match/5"
params = {
    "page": "2",
    'm': int(time.time()*1000),
    'f': int(time.time())*1000
}

# print(int(time.time())*1000)
# response = requests.get(url, headers=headers, cookies=cookies, params=params)
# print(response.text)
# print(response)



