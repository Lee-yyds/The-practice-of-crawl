from fontTools.ttLib import TTFont
import requests


def font_dic(woff_file):
    font = TTFont(woff_file)
    font_dict = {}
    # 获取对应关系
    code_name = font.getBestCmap()
    real_dict = {'uniE1D0': 8, 'uniE325': 2, 'uniE41D': 3, 'uniE52E': 4, 'uniE630': 5, 'uniE76E': 7, 'uniE891': 1,
                 'uniE9CE': 0, 'uniEAF2': 9, 'uniEC4C': 6}
    for k, v in code_name.items():
        if v in real_dict:
            font_dict['&#'+str(k)+';'] = str(real_dict[v])
    return font_dict


def get_data():
    headers = {
        "authority": "mapi.guazi.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "anti-token": "1277105907",
        "cache-control": "no-cache",
        "client-time": "1664602026",
        "client-timestamp": "1664602025",
        "origin": "https://www.guazi.com",
        "platform": "5",
        "pragma": "no-cache",
        "referer": "https://www.guazi.com/",
        "sec-ch-ua": "^\\^Microsoft",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "szlm-id": "D2If+rzz2lapbO2NXFIXMUgu23olw5fq84qqu4zowLFEUX3b",
        "token": "",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
        "verify-token": "ae64c204bea5340651645222d7cd5b34"
    }
    cookies = {
        "uuid": "022b2dd2-79f0-4f0c-94d9-dcd54796892b",
        "cainfo": "^%^7B^%^22ca_s^%^22^%^3A^%^22self^%^22^%^2C^%^22ca_n^%^22^%^3A^%^22self^%^22^%^2C^%^22ca_medium^%^22^%^3A^%^22-^%^22^%^2C^%^22ca_term^%^22^%^3A^%^22-^%^22^%^2C^%^22ca_content^%^22^%^3A^%^22-^%^22^%^2C^%^22ca_campaign^%^22^%^3A^%^22-^%^22^%^2C^%^22ca_kw^%^22^%^3A^%^22-^%^22^%^2C^%^22ca_i^%^22^%^3A^%^22-^%^22^%^2C^%^22scode^%^22^%^3A^%^22-^%^22^%^2C^%^22guid^%^22^%^3A^%^22022b2dd2-79f0-4f0c-94d9-dcd54796892b^%^22^%^7D",
        "sessionid": "3ded9cfb-3cc8-4a04-dd37-9c2fccc67715"
    }
    url = "https://mapi.guazi.com/car-source/carList/pcList"
    params = {
        "versionId": "0.0.0.0",
        "sourceFrom": "wap",
        "deviceId": "022b2dd2-79f0-4f0c-94d9-dcd54796892b",
        "osv": "Windows 10",
        "minor": "",
        "sourceType": "",
        "ec_buy_car_list_ab": "",
        "location_city": "",
        "district_id": "",
        "tag": "-1",
        "license_date": "",
        "auto_type": "",
        "driving_type": "",
        "gearbox": "",
        "road_haul": "",
        "air_displacement": "",
        "emission": "",
        "car_color": "",
        "guobie": "",
        "bright_spot_config": "",
        "seat": "",
        "fuel_type": "",
        "order": "",
        "priceRange": "0,-1",
        "tag_types": "",
        "diff_city": "",
        "intention_options": "",
        "initialPriceRange": "",
        "monthlyPriceRange": "",
        "transfer_num": "",
        "car_year": "",
        "carid_qigangshu": "",
        "carid_jinqixingshi": "",
        "cheliangjibie": "",
        "page": "1",
        "pageSize": "20",
        "city_filter": "12",
        "city": "12",
        "guazi_city": "12",
        "qpres": "",
        "platfromSource": "wap"
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    return response.json()


def parse_data(data):
    data_list = data['data']['postList']
    a = font_dic('gzfont3.woff2')

    for j in data_list:
        pay = j['first_pay']
        title = j['title']
        for i in a:
            pay = pay.replace(i, a[i])
        print(title, pay)

if __name__ == '__main__':
    dt = get_data()
    parse_data(data=dt)

