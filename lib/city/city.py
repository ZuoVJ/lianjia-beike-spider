#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 城市缩写和城市名的映射
# 想抓取其他已有城市的话，把相关城市信息放入下面的字典中

cities = {
    'bj': '北京',
    'cd': '成都',
    'cq': '重庆',
    'cs': '长沙',
    'dg': '东莞',
    'dl': '大连',
    'fs': '佛山',
    'gz': '广州',
    'hz': '杭州',
    'hf': '合肥',
    'jn': '济南',
    'nj': '南京',
    'qd': '青岛',
    'sh': '上海',
    'sz': '深圳',
    'su': '苏州',
    'sy': '沈阳',
    'tj': '天津',
    'wh': '武汉',
    'xm': '厦门',
    'yt': '烟台',
}


def get_chinese_city(en):
    """
    拼音拼音名转中文城市名
    :param en: 拼音
    :return: 中文
    """
    return cities.get(en, None)


if __name__ == '__main__':
    print get_chinese_city("sh")
