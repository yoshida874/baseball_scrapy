# -*- coding: utf-8 -*-
import scrapy

from baseball.items import BatterItem;

class PacificSpider(scrapy.Spider):
    name = 'pacific'
    allowed_domains = ['npb.jp']
    start_urls = ['http://npb.jp/bis/2019/stats/bat_p.html']

    def parse(self, response):
        for tr in response.xpath('//*[@id="stdivmaintbl"]/table').xpath('tr'):

            item = BatterItem()
            if not isinstance(tr.xpath('td[2]/text()').extract_first(),type(None)):
                name_str = tr.xpath('td[2]/text()').extract_first()
                    #全角空白の削除
                item['name'] = name_str.replace('　', ' ')
                item['AVG'] = tr.xpath('td[4]/text()').extract_first()
                item['bat'] = tr.xpath('td[6]/text()').extract_first()
            yield item
