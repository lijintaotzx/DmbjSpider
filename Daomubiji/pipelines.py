# -*- coding: utf-8 -*-
import os
from .settings import BOOK_BASE_PATH


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DaomubijiPipeline(object):
    def get_book_path(self, item):
        book_path = BOOK_BASE_PATH + item['book_name'] + '/'
        if not os.path.exists(book_path):
            os.makedirs(book_path)
        return book_path

    def process_item(self, item, spider):
        book_path = self.get_book_path(item)
        filename = book_path + item['article_title'] + '.txt'
        with open(filename, 'w') as f:
            f.write(item['article_content'])

        return item
