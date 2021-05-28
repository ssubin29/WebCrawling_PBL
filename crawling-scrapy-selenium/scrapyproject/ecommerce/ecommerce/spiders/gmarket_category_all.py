# -*- coding: utf-8 -*-
import scrapy
from ecommerce.items import EcommerceItem

class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'

    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback=self.parse_mainpages)

    def parse_mainpages(self, response):
        print("parse_mainpages")
        category_links = response.css('div.gbest-cate ul.by-group li a::attr(href)').getall()
        category_names = response.css('div.gbest-cate ul.by-group li a::text').getall()

        # 1st category crawling
        for index, category_link in enumerate(category_links):
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link, callback=self.parse_items, meta={'main_category_name':category_names[index], 'sub_category_name': 'ALL' })
        # 2nd category crawling
        for index, category_link in enumerate(category_links):
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link, callback=self.parse_subcategory, meta={'main_category_name':category_names[index] })


    def parse_subcategory(self, response):
        print ("parse_subcategory", response.meta['main_category_name'])
        subcategory_links = response.css('div.navi.group > ul > li > a::attr(href)').getall()
        sub_category_names = response.css('div.navi.group > ul > li > a::text').getall()
        for index, subcategory_link in enumerate(subcategory_links):
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + subcategory_link, callback=self.parse_items, meta={'main_category_name':response.meta['main_category_name'], 'sub_category_name':sub_category_names[index] })


    def parse_items(self, response):
        print ("parse_maincategory", response.meta['main_category_name'], response.meta['sub_category_name'])

        best_items = response.css('div.best-list')
        for index, item in enumerate(best_items[1].css('li')):
            doc = EcommerceItem()
            ranking = index + 1
            title = item.css('a.itemname::text').get()
            ori_price = item.css('div.o-price::text').get()
            dis_price = item.css('div.s-price strong span span::text').get()
            discount_percent = item.css('div.s-price em::text').get()

            if ori_price == None:
                ori_price = dis_price
            ori_price = ori_price.replace(",", "").replace("원", "")
            dis_price = dis_price.replace(",", "").replace("원", "")
            if discount_percent == None:
                discount_percent = '0'
            else:
                discount_percent = discount_percent.replace("%", "")

            doc['main_category_name'] = response.meta['main_category_name']
            doc['sub_category_name'] = response.meta['sub_category_name']
            doc['ranking'] = ranking
            doc['title'] = title
            doc['ori_price'] = ori_price
            doc['dis_price'] = dis_price
            doc['discount_percent'] = discount_percent
            #print (ranking, title, ori_price, dis_price, discount_percent)
            yield doc