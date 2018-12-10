#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import threading

import requests
from lxml import etree

baseUrl = "https://gank.io"
path = "E:/tempImg/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}


def save_img(url):
    """
    将图片保存到本地
    :param url:
    :return:
    """
    r = requests.get(url, stream=True)
    with open(path + url.split('/')[-1], 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)


def gank_spider(url):
    """
    爬取gank数据 获取下一页
    """
    print(url)
    r = requests.get(url)
    content = r.text
    # print(content)
    selector = etree.HTML(content)
    result = selector.xpath('//div[@class="row"]/div/p/a/@href')
    img_url = selector.xpath('//div/div/p/img/@src')[0]
    next_url = result[-1]
    # print(result)
    print(next_url)
    print(img_url)
    save_img(img_url)
    # 多线程
    t = threading.Thread(target=save_img, args=(img_url,))
    t.start()
    gank_spider(baseUrl + next_url)


if __name__ == "__main__":
    full_url = baseUrl
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录 , 创建目录操作函数
        os.makedirs(path)
    gank_spider(full_url)
