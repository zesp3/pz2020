import scrapy

from scrapy import cmdline
class KontaktySpider(scrapy.Spider):
    name = 'kontakty'
    allowed_domains = ['lubianka.pl/9478,urzad-gminy']
    start_urls = ['https://www.lubianka.pl/9478,urzad-gminy']

    def parse(self, response):
        for i in response.css('div.system_anchor'):
             yield {
                        'text': i.css('span::text').getall(),
            }


cmdline.execute("scrapy crawl kontakty -o kontakty.json -t json".split())