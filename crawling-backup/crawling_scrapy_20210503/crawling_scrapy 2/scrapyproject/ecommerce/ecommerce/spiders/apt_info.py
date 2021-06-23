# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class AptInfoSpider(scrapy.Spider):
    name = 'apt_info'
    start_urls = ['http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade']

    def start_requests(self):
        service_key = '71tM1D3BN3EOZtG%2BCoiLLfRIp2Or4R3MfMxqWBheReAfT7y4%2BC7ZBtLwrZ%2F2cxm9vV3pz3etps9yJcwbiPAtBQ%3D%3D'
        location_code = '11110'
        deal_date = '201906'
        open_api = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'

        for url in self.start_urls:
        	request_api = url + '?LAWD_CD=' + location_code + '&DEAL_YMD=' + deal_date + '&serviceKey=' + service_key
        	yield scrapy.http.Request(request_api)

    def parse(self, response):
    	soup = BeautifulSoup(response.text, 'xml')
    	items = soup.find_all('item')
    	for item in items:
    		print (item.find('거래금액').get_text(), item.find('아파트').get_text(), item.find('전용면적').get_text())
