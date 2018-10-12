#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 20:00
# @Author  : hulin.tech
# @File    : DownMusic.py

import json

import requests

url = "http://music.zhuolin.wang/api.php?callback=jQuery111306976373105974689_1539309667922"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01'}


def down_music(name, down_url):
    """
    根据url下载music到当前目录,保存文件为name
    :param name:
    :param down_url:
    :return:
    """
    print("==> downloading %s  -> %s" % (name, down_url))
    down_request = requests.get(down_url, headers=headers)
    with open(name, "wb") as code:
        code.write(down_request.content)
    print("==> download complete %s " % (name,))


def parse_music_list(json_content):
    """
    解析返回的字符串转成歌曲列表
    :param json_content: dict
    :return:
    """
    # 从数据中取中歌曲list
    music_list = json_content['playlist']['tracks']
    # print(music_list)
    # print(len(music_list))
    for music in music_list:
        # 歌曲名
        name = music['name']
        # 歌手
        author = music['ar'][0]['name']
        # 歌曲id , 在请求获取下载链接时需要此id作为参数
        music_id = music['id']
        # 组装获取下载链接的参数
        down_url_params = {"types": "url", "id": music_id, "source": "netease"}
        down_r = requests.post(url=url, params=down_url_params, headers=headers)
        url_content_json = sub_string_to_json(down_r.text)
        down_url = url_content_json['url']
        print("==> %s -> %s -> %s" % (name, author, down_url))
        music_name = "%s-%s.mp3" % (name, author)
        down_music(music_name, down_url)


def sub_string_to_json(pre_text):
    """
    将字符串处理成json格式返回 , 这里返回的是原生类型dict
    :param pre_text:
    :return:
    """
    pre_text = pre_text[pre_text.find('{'): len(pre_text) - 1]
    if pre_text.endswith(")"):
        pre_text = pre_text[:len(pre_text) - 1]
    # 将str转成json, 这里会成为原生类型,即dict
    json_content = json.loads(pre_text)
    return json_content


if __name__ == "__main__":
    params = {"types": "playlist", "id": "3778678"}

    r = requests.post(url=url, params=params, headers=headers)

    print(r.status_code)
    # print(r.text)
    # 对返回的内容需要截取掉多余的部分保证是一个完整的json格式
    content = sub_string_to_json(r.text)
    # 解析数据
    parse_music_list(content)
