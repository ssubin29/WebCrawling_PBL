# -*- coding: utf-8 -*-
import scrapy
import json
import re

class NaverSpider(scrapy.Spider):
    name = 'naver'
    start_urls = ['https://openapi.naver.com/v1/search/shop.json?query=']

    def start_requests(self):
        client_id = 'qs73qpiHimZzpI_RrTF7'
        client_secret = 'pSVWxZtUzQ'
        header_params = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}
        query = 'iphone'
        for url in self.start_urls:
            yield scrapy.http.Request(url + query, headers=header_params)

    def parse(self, response):
        data = json.loads(response.body_as_unicode())
        for item in data['items']:
        	print (re.sub('<\S+>', '', item['title']))
