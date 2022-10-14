import execjs
import requests


def get_data(page):
    global sum
    with open("nixiang.js", 'r') as f:
        js_code = f.read()

    ctx = execjs.compile(js_code)
    signature = ctx.call('anonymous')
    # print(signature)
    headers = {
        "Origin": "http://spider.wangluozhe.com",
        "Referer": "http://spider.wangluozhe.com/challenge/2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42",
    }
    cookies = {
        "session": "d53f8e4d-f3dd-41d1-90c4-3493594a0415.FAjhwHfuZ83qe5iz8Hhj_UdU33I"
    }
    url = "http://spider.wangluozhe.com/challenge/api/2"
    data = {
        "page": page,
        "count": "10",
        "_signature": signature
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False).json()
    data_list = response['data']
    for item in data_list:
        a = item['value']
        sum += a
    print(sum)


if __name__ == '__main__':
    sum = 0
    for i in range(1, 101):
        get_data(i)
    print(sum)
