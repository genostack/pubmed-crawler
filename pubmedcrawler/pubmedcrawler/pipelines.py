# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib
import logging

class PubmedcrawlerPipeline(object):
    def process_item(self, item, spider):
        file_name = hashlib.sha224(item['article']).hexdigest() + '.xml.gz'
        with open('files/%s' % file_name, 'w+b') as f:
            f.write(item['article'])
        return item
