# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()


            # absalute_url = f"https://www.worldometers.info{link}"
            # absalute_url = response.urljoin(link)

            # yield scrapy.Request(url=absalute_url)
            yield response.follow(url=link)
