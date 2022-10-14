import os
import requests
from fontTools.ttLib import TTFont


def parse_data(data_url, content_str):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    }
    world_content = requests.get(url=data_url, headers=headers).content
    # 对获取到的字体进行下载..........
    with open('./world.ttf', 'wb') as f:
        f.write(world_content)
    # 那么便开始通过字体库进行解析
    world = TTFont('./world.ttf')
    os.remove('./world.ttf')
    # 读取响应的映射关系
    uni_list = world['cmap'].tables[0].ttFont.getGlyphOrder()
    unicode_list = [eval(r"u'\u" + uni[3:] + "'") for uni in uni_list[1:]]
    world_list = ["真", "少", "多", "三", "不", "是", "四", "右", "七", "盘", "很", "坏", "味", "公",
                  "短", "排", "油", "路", "远", "坐", "加", "身", "二", "耗", "低", "光", "更",
                  "内", "八", "孩", "中", "性", "好", "皮", "副", "下", "六", "空", "小", "比", "得", "硬", "启", "电",
                  "大", "养", "泥", "门", "响", "控", "软", "外", "五", "一", "十", "自", "雨", "地", "长", "高", "有",
                  "和",
                  "上", "过", "级", "档", "呢", "动", "左", "进", "的", "着", "机", "开", "里", "了", "当", "矮", "只",
                  "无", "音", "手", "九", "问", "灯", "冷", "实", "保", "来", "量"]  # 录入字体文件中的字符
    for i in range(len(unicode_list)):
        content_str = content_str.replace(unicode_list[i], world_list[i])
    return content_str
