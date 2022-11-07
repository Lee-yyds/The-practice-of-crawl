import requests
from base64 import b64encode


def send_req(page):
    message = 'yuanrenxue' + str(page)
    m = b64encode(message.encode())
    headers = {
        "referer": "https://match.yuanrenxue.com/match/12",
        'User-Agent': 'yuanrenxue.project'
    }
    cookies = {

        "sessionid": "w1yv1qpvajkxn5gu11w3o4wyq01khtmv"
    }
    params = {
        'page': page,
        'm': m.decode()
    }
    url = "https://match.yuanrenxue.com/api/match/12"
    res = requests.get(url=url, headers=headers, params=params, cookies=cookies)
    dt_li = res.json()['data']
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




