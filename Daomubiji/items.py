# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomubijiItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_url = scrapy.Field()
    article_url = scrapy.Field()
    article_title = scrapy.Field()
    article_content = scrapy.Field()
