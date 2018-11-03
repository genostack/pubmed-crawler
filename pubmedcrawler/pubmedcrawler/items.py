# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class PubmedcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pmid = Field()
    article_title = Field()
    abstract = Field()
    author = Field()
    full_text_url = Field()
    date_time = Field()
    article = Field()
    pass
