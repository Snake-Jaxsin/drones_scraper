import scrapy


class DronesSpider(scrapy.Spider):
    name = 'drones'
    start_urls = ['https://www.jessops.com/drones/']

    def parse(self, response):
        for products in response.css('div.details-pricing'):
            yield {
                "title": products.css('a::text').get(),
                "price": products.css('p.price.larger::text').get(),
                "link": products.css('a::attr(href)').get()
            }
