import scrapy
import re

class SzkolySpider(scrapy.Spider):
    name = 'szkola'
    start_urls = ['https://www.lubianka.pl/9439,oswiata']

    def parse(self, response):
        quote = response.xpath('//div[@id="akapit_29609"]')
        links = quote.xpath('//a[contains(@href, "http")]')
        przedszkola = quote.xpath('//a[contains(@href, "facebook")]')
        reg = re.compile("Szkoła *")
        regPrzedszkola = re.compile(" *rzedszkole *")
        for index, link in enumerate(links):
            if reg.search(str(link.xpath('text()').get())):
                yield {
                    'href': link.xpath('@href').get(),
                    'name': link.xpath('text()').get(),
                }

        for index, przedszkole in enumerate(przedszkola):
            if regPrzedszkola.search(str(przedszkole.xpath('text()').get())):
                yield {
                    'href': przedszkole.xpath('@href').get(),
                    'name': przedszkole.xpath('text()').get(),
                }


