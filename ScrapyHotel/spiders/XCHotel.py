# -*- coding: utf-8 -*-
import json
import re

import scrapy

from ScrapyHotel.items import ScrapyhotelItem
import time

class XchotelSpider(scrapy.Spider):
    name = 'XCHotel'
    start_urls = ['https://hotels.ctrip.com/']

    def start_requests(self):
        self.headers = {
            'Referer': 'https://www.ctrip.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        yield scrapy.Request('https://hotels.ctrip.com/Domestic/Tool/AjaxGetCitySuggestion.aspx', headers=self.headers,
                             callback=self.parseCity)



    def parseCity(self, response):
        self.item = ScrapyhotelItem()
        citySub = response.text
        cityName = []
        cityNumber = []
        cityPY = []
        citySub = re.findall('data:"(.*?)"', citySub,re.S)
        for s in citySub:
            ss = s.split('|')
            cityPY.append(ss[0])
            cityName.append(ss[1])
            cityNumber.append(ss[2])
        self.item['cityPy'] = cityPY
        self.item['cityName'] = cityName
        self.item['cityId'] = cityNumber

        for i in self.item['cityId']:
            url = 'https://hotels.ctrip.com/Domestic/Tool/AjaxGetHotKeyword.aspx?cityid={id}'.format(id=i)
            print(i,'爬取商圈分类',url)
            yield scrapy.Request(url=url, headers=self.headers,callback=self.parseSQ)
            time.sleep(5)

    def parseSQ(self, response):
        data = response.text
        shangId = re.findall('id":"(.*?)",',data,re.S)
        shangName = re.findall('"name":"(.*?)",', data, re.S)
        # self.item['shangIdNmuber']=response.meta['id']
        self.item['shangId'] = shangId
        self.item['shangName'] = shangName
        yield self.item