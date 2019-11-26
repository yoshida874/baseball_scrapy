# -*- coding: utf-8 -*-
import scrapy

from baseball.items import BatterItem;

class BatterSpider(scrapy.Spider):
    name = 'batter'
    allowed_domains = ['npb.jp']
    start_urls = ['http://npb.jp/bis/2019/stats/idb2_db.html']

    def parse(self, response):
        for tr in response.xpath('//*[@id="stdivmaintbl"]/table').xpath('tr'):
            item = BatterItem()

            item['name']= tr.xpath('td[2]/text()').extract_first()
            """
            item['game']= tr.xpath('td[3]/text()').extract_first()
            item['ba']=tr.xpath('td[4]/text()').extract_first()
            """
            yield item
