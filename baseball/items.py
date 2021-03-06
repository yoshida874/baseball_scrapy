# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy import Item, Field

class VbItem(Item):
    name = Field()      # 名前
    bat = Field()       # 右打ち or 左打ち or 両打ち
    pit = Field()       #右投げ or 左投げ
    number = Field()    #背番号
    day = Field()       #誕生日
    height = Field()    #身長
    weight = Field()    #体重

class BatterItem(Item):
    name = Field()      # 名前
    team = Field()      #チーム
    AVG = Field()       #打率
    game = Field()
    #bat = Field()       #打席数
    long_hit = Field()  #長打率
    spawn = Field()     #出塁率