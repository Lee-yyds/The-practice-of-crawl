from fontTools.ttLib import TTFont


def font_dic(woff_file):
    # 加载字体文件：
    font = TTFont(woff_file)
    font_dict = {}
    # 获取对应关系
    code_name = font.getBestCmap()
    for k, v in code_name.items():
        # print(k, v)
        # print(hex(k), v)
        if v[3:]:
            cont = '\\u00' + v[3:] if len(v[3:]) ==2 else '\\u' + v[3:]
            real_content = cont.encode('utf-8').decode('utf-8')
            k_hex = hex(k)
            rea_k = k_hex.replace('0x', '&#x')
            font_dict[rea_k] = real_content
    return font_dict


if __name__ == '__main__':
    a = font_dic('file.woff')
    print(a)


