import scrapy
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
import requests
import pandas as pd


class MimSpider(scrapy.Spider):
    name = 'mim'
    allowed_domains = ['www.tsetmc.com']
    start_urls = ['http://www.tsetmc.com/']

    body = requests.get('http://tsetmc.com/').content
    response = HtmlResponse(url='http://tsetmc.com/', body=body)
    def parse(self, response):
        table = response.css('table').getall()
        for item in table:
            print (item)