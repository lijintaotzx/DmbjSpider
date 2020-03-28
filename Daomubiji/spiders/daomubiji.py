# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomubijiItem


class DaomubijiSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        books = []
        book_list = response.xpath('//ul/li')
        for book in book_list:
            item = DaomubijiItem()

            item['book_name'] = book.xpath('./a/text()').get()
            item['book_url'] = book.xpath('./a/@href').get()
            if item['book_url']:
                books.append(item)
        for book in books:
            yield scrapy.Request(url=book['book_url'], meta={'book': book}, callback=self.parse_article)

    def parse_article(self, response):
        book = response.meta['book']
        articles = []
        article_list = response.xpath('//div[@class="excerpts"]/article')
        for article in article_list:
            item = DaomubijiItem()
            item['article_url'] = article.xpath('./a/@href').get()
            item['article_title'] = article.xpath('./a/text()').get()
            item['book_name'] = book['book_name']
            item['book_url'] = book['book_url']

            articles.append(item)

        for article in articles:
            yield scrapy.Request(
                url=article['article_url'],
                meta={'article': article},
                callback=self.get_article_content
            )

    def get_article_content(self, response):
        article = response.meta['article']
        content = response.xpath('//article[@class="article-content"]//p/text()')
        article['article_content'] = '\n'.join(content.extract())

        yield article
