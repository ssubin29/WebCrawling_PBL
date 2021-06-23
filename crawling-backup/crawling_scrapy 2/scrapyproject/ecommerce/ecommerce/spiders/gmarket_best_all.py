# -*- coding: utf-8 -*-
import scrapy
from ecommerce.items import EcommerceItem


class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_best_all'

    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback=self.parse_mainpages)

    def parse_mainpages(self, response):
        print("parse_mainpages")
        category_links = response.css(
            'div.gbest-cate ul.by-group li a::attr(href)').getall()
        category_names = response.css(
            'div.gbest-cate ul.by-group li a::text').getall()
        for index, category_link in enumerate(category_links):
            # category_names[index]
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link, callback=self.parse_maincategory, meta={'maincategory_name': category_names[index]})

        for index, category_link in enumerate(category_links):
            # category_names[index]
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + category_link, callback=self.parse_subcategory, meta={'maincategory_name': category_names[index]})

    def parse_subcategory(self, response):
        print('parse_subcategory', response.meta['maincategory_name'])
        subcategories = response.css(
            'div.navi.group ul li > a::attr(href)').getall()
        subcategory_names = response.css(
            'div.navi.group ul li > a::text').getall()
        for num, subcategory in enumerate(subcategories):
            print('subcategory', 'http://corners.gmarket.co.kr' + subcategory,
                  response.meta['maincategory_name'], subcategory_names[num])
            yield scrapy.Request(url='http://corners.gmarket.co.kr' + subcategory, callback=self.parse_maincategory, meta={'maincategory_name': response.meta['maincategory_name'], 'subcategory_name': subcategory_names[num]})

    def parse_maincategory(self, response):
        print("parse_maincategory", response.meta['maincategory_name'])

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

            yield doc
            #print (ranking, title, ori_price, dis_price, discount_percent)
