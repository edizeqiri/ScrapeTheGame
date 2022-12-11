import scrapy
from bs4 import BeautifulSoup


class Spiderman(scrapy.Spider):
    name = 'spiderman'

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.tutti.ch/de/q/suche?sorting=newest&page=1&query=canon',
            callback=self.parse)

    def parse(self, response):
        # get nice html
        soup = BeautifulSoup(response.text, 'html.parser')
        # get all hrefs
        a = scrapy.Selector(response).xpath('//a/@href').getall()
