# -*- coding: utf-8 -*-
import scrapy

from baseball.items import BatterItem;

class BatterSpider(scrapy.Spider):
    name = 'DeNA'
    allowed_domains = ['npb.jp']
    start_urls = ['http://npb.jp/bis/teams/rst_db.html']

    def parse(self, response):

       #//＝ノードの省略 @=クラス要素の指定
       for tr in response.xpath('//*[@id="tedivmaintbl"]/div[4]/table').xpath('tr'):
            
            item = BatterItem()
            
            item['number'] = tr.xpath('td[1]/text()').extract_first()
            #if文で値がnullかを判断する
            if not isinstance(tr.xpath('td[2]/a/text()').re_first(r'\w+\s*\w+'),type(None)):
                name_str = tr.xpath('td[2]/a/text()').re_first(r'\w+\s*\w+')
                #全角空白の削除
                item['name'] = name_str.replace('　', ' ')
    
            item['day'] = tr.xpath('td[3]/text()').extract_first()
            item['height'] = tr.xpath('td[4]/text()').extract_first()
            item['weight'] = tr.xpath('td[5]/text()').extract_first()
            item['pit'] = tr.xpath('td[6]/text()').extract_first()
            item['bat'] = tr.xpath('td[7]/text()').extract_first()
            
            yield item
            