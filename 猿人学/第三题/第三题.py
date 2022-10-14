import requests


def get_data(page):
    proxies = {
        'http': 'http://localhost:8889',
        'https': 'http://localhost:8889'
    }
    headers = {
        # ':authority': 'match.yuanrenxue.com',
        # ':method': 'GET',
        # ':path': '/api/match/3?page=3',
        # ':scheme': 'https',
        # 'accept': 'application/json, text/javascript, */*; q=0.01',
        # 'accept-language': 'zh-CN,zh;q=0.9',
        # 'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'yuanrenxue.project',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://match.yuanrenxue.com/match/3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',

    }
    headers1 = {
        "content-length": "0",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37",
        "sec-ch-ua-platform": "Windows",
        "accept": "*/*",
        "origin": "https://match.yuanrenxue.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://match.yuanrenxue.com/match/3",
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        # 'cookie':'sessionid=s135ehicqjkoq3wkmry6n5iubnt0a2uf; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1665461809,1665462165,1665551425; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1665551425; qpfccr=true; no-alert3=true',


    }
    cookies = {
        "sessionid": "s135ehicqjkoq3wkmry6n5iubnt0a2uf",
        "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1665461809,1665462165,1665551425",
        "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1665551425",
        "qpfccr": "true",
        "no-alert3": "true"
    }
    url = f"https://match.yuanrenxue.com/api/match/3?page={page}"
    url1 = 'https://match.yuanrenxue.com/jssm'
    session = requests.session()
    session.headers = headers1
    res1 = session.post(url=url1, cookies=cookies,proxies=proxies, verify=False)
    # print(res1.cookies)
    response = session.get(url=url, headers=headers, cookies=cookies, proxies=proxies, verify=False)
    # print(response.text)
    # print(response)
    return response.json()


if __name__ == '__main__':
    data_list = []
    for i in range(1,6):
        data = get_data(i)
        for j in data['data']:
            data_list.append(j['value'])
    print(data_list)
    print(max(data_list, key=data_list.count))





