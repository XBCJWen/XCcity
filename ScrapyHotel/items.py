# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyhotelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cityPy = scrapy.Field()
    cityName = scrapy.Field()
    cityId = scrapy.Field()
    # shangIdNmuber = scrapy.Field()
    shangId = scrapy.Field()
    shangName = scrapy.Field()

