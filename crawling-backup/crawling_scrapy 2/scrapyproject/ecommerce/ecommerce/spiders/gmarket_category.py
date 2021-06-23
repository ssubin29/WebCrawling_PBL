# -*- coding: utf-8 -*-
import scrapy


class GmarketCategorySpider(scrapy.Spider):
    name = 'gmarket_category'
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G']

    def start_requests(self):
        for url in self.start_urls:
            for index in range(1, 13):
                yield scrapy.http.Request(url + '{0:02d}'.format(index))

    def parse(self, response):
    	print (response.url)
