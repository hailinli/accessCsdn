#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/24 下午8:39
# @Author  : Lihailin<415787837@qq.com>
# @Desc    : 
# @File    : aceessCsdn.py
# @Software: PyCharm
from lxml import etree
import crawBase
import time

class AccessCsdn(crawBase.CrawBase):
    '''
    访问csdn
    '''
    def getArticals(self, url):
        '''
        https://blog.csdn.net/linhai1028/article/list/2
        解析所有博客链接
        :param urls:
        :return:
        '''
        c = self.get(url)
        html = etree.HTML(c)
        l = html.xpath('//div[@class="article-list"]//a/@href')
        # print(l)
        return l

    def geAllArticals(self, urlBase):
        '''
        https://blog.csdn.net/linhai1028/article/list/1
        list第
        解析所有博客链接
        :param urlBase:
        :return:
        '''
        i = 1
        urls = []
        url = urlBase
        while True:
            # print('sfs'+url)
            t = self.getArticals(url)
            urls += t
            if len(t) == 0:
                break
            i += 1
            url = urlBase + '/article/list/%s' % i
        return urls

    def run(self, url, sec):
        '''
        刷url链接文章
        :param url:
        :param sec: 间隔时间
        :return:
        '''
        urls = self.geAllArticals(url)
        urls = list(set(urls))
        # print(len(urls))
        while True:
            for url in urls:
                # print(url)
                self.get(url)
            time.sleep(sec)

if __name__ == '__main__':
    url = "https://blog.csdn.net/linhai1028/"
    accessCsdn = AccessCsdn()
    accessCsdn.run(url, 40)