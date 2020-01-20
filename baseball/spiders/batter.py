# -*- coding: utf-8 -*-
import scrapy

from baseball.items import BatterItem;

class BatterSpider(scrapy.Spider):
    name = 'batter'
    allowed_domains = ['npb.jp']
    start_urls = ['http://npb.jp/bis/2019/stats/bat_p.html']

    def parse(self, response):
        for tr in response.xpath('//*[@id="stdivmaintbl"]/table').xpath('tr'):
            item = BatterItem()

            item['name']= tr.xpath('td[2]/text()').extract_first()
            item['team'] = tr.xpath('td[3]/text()').extract_first()
            item['AVG']= tr.xpath('td[4]/text()').extract_first()
            item['game']=tr.xpath('td[5]/text()').extract_first()
            item['long_hit']=tr.xpath('td[24]/text()').extract_first()
            item['spawn']=tr.xpath('td[25]/text()').extract_first()

            yield item
