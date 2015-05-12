import scrapy


class ImajiSpider(scrapy.Spider):
    name = "imaji"
    allowed_domains = ["google.com"]
    start_urls = ["http://www.google.com"]

    def parse(self, response):
        print('Title:', response.xpath('//title/text()').extract()[0])
        print('Images:', response.xpath('//img/@src').extract())
        print('Styles (files):', response.xpath('//link[contains(@href, ".css")]/@href').extract())
        print('Styles (inline):', response.xpath('//style/text()').extract())
