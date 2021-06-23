# -*- coding: utf-8 -*-
import scrapy
from ecommerce.items import EcommerceItem

class GmarketBestSpider(scrapy.Spider):
    name = 'gmarket_best'

    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        # 2021.05.03 해당 사이트의 li 태그가 변경되어, 기존 li[id] 를 li 로 변경하였습니다. 참고부탁드립니
        #titles = response.css('div.best-list > ul > li[id] > a::text').getall()
        #prices = response.css('div.best-list > ul > li[id] > div.item_price > div.s-price > strong > span > span::text').getall()
        
        titles = response.css('div.best-list > ul > li > a::text').getall()
        prices = response.css('div.best-list > ul > li > div.item_price > div.s-price > strong > span > span::text').getall()
        for num, title in enumerate(titles):
            doc = EcommerceItem()
            doc['title'] = title
            doc['price'] = prices[num].strip().replace("원", "").replace(",", "")
            yield doc



