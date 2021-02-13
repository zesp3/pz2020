import scrapy

class SzkolniakiSpider(scrapy.Spider):
    name = 'szkolniak'
    start_urls = ['https://www.lubianka.pl/9452,gminna-komunikacja-autobusowa']
    start = ['https://www.lubianka.pl']

    def parse(self, response):
        for q in response.css('div.galeria_grafika_box').css('a::attr(href)').getall():
            yield{
                'link': self.start[0] + q
            }
