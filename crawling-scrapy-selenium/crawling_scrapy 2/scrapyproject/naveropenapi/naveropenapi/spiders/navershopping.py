# -*- coding: utf-8 -*-
import scrapy
import json
from naveropenapi.items import NaveropenapiItem

class NavershoppingSpider(scrapy.Spider):
    name = 'navershopping'

    def start_requests(self):
        start_url = 'https://openapi.naver.com/v1/search/shop.json?query='
        client_id = 'qs73qpiHimZzpI_RrTF7'
        client_secret = 'pSVWxZtUzQ'
        header_params = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}
        query = 'iphone'
        for index in range(10):
            yield scrapy.Request(url=start_url + query + '&display=100&start=' + str(index*100 + 1), headers=header_params)

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        for item in data['items']:
            doc = NaveropenapiItem()
            doc['title'] = item['title']
            doc['link'] = item['link']
            doc['image'] = item['image']
            doc['lprice'] = item['lprice']
            doc['hprice'] = item['hprice']
            doc['mallName'] = item['mallName']
            doc['productId'] = item['productId']
            doc['productType'] = item['productType']
            yield doc
