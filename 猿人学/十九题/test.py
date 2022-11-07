import requests


headers = {
    "Host": "match.yuanrenxue.com",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://match.yuanrenxue.com/match/19",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
}
cookies = {
    "qpfccr": "true",
    "no-alert3": "true",
    "tk": "5250545942679202732",
    "sessionid": "w1yv1qpvajkxn5gu11w3o4wyq01khtmv"
}
url = "https://match.yuanrenxue.com/api/match/19"
params = {
    "page": "1"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)

