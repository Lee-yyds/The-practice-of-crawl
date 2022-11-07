import httpx


def send_req(page):
    client = httpx.Client(http2=True)
    headers = {
        "authority": "match.yuanrenxue.com",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://match.yuanrenxue.com/match/17",
        "sec-ch-ua": "^\\^Microsoft",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "yuanrenxue.project",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = {
        "qpfccr": "true",
        "no-alert3": "true",
        "tk": "5250545942679202732",
        "sessionid": "w1yv1qpvajkxn5gu11w3o4wyq01khtmv"
    }
    url = "https://match.yuanrenxue.com/api/match/17"
    params = {
        "page": page
    }
    response = client.get(url=url, params=params, headers=headers, cookies=cookies)
    dt_li = response.json()['data']
    in_total = 0
    for item in dt_li:
        number = item['value']
        print(number)
        in_total += int(number)
    return in_total


if __name__ == '__main__':
    total = 0
    for i in range(1, 6):
        num = send_req(i)
        total += num
        print(f'第{i}页和', total)
    print(total)

