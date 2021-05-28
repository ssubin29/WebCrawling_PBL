# -*- coding: utf-8 -*-
import scrapy
from ecommerce.items import EcommerceItem

class GmarketBestSpider(scrapy.Spider):
    name = 'gmarket_best'

    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list > ul > li[id] > a::text').getall()
        prices = response.css('div.best-list > ul > li[id] > div.item_price > div.s-price > strong > span > span::text').getall()
        for num, title in enumerate(titles):
            doc = EcommerceItem()
            doc['title'] = title
            doc['price'] = prices[num].strip().replace("원", "").replace(",", "")
            yield doc



