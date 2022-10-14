import requests


headers = {
    "accesstoken": "ENO4DIENKUPRBLGY7H6PYQHDGPUQBHWQVVYP26QUJMCJINFZFVLA113ad02",
    "referer": "https://mobile.yangkeduo.com/goods_comments.html?goods_id=342850724813&thumb_url=https^%^3A^%^2F^%^2Fimg.pddpic.com^%^2Fgaudit-image^%^2F2022-03-29^%^2F5a705abe588dcb6fb99cfd519313f279.jpeg^%^3FimageView2^%^2F2^%^2Fw^%^2F1300^%^2Fq^%^2F80&refer_page_el_sn=96513&page_from=402&refer_page_name=goods_detail&refer_page_id=10014_1663338745644_wmaa5fcrhi&refer_page_sn=10014&mall_id=782448287",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.33"
}

url = "https://mobile.yangkeduo.com/proxy/api/reviews/342850724813/list"
params = {
    "pdduid": "4260609434541",
    "page": "3",
    "size": "10",
    "enable_video": "1",
    "enable_group_review": "1",
    "label_id": "0"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)