import scrapy
from kontakt.items import KontaktItem


class KontaktySpider(scrapy.Spider):
    name = 'kontakty'
    allowed_domains = ['lubianka.pl/9478,urzad-gminy']
    start_urls = ['https://www.lubianka.pl/9478,urzad-gminy']

    def parse(self, response):
        quote = response.xpath('//div[@id="akapit_29685"]')
        item_zawartosc = quote.css('span::text').getall(),
        kontaktItem = KontaktItem(zawartosc = item_zawartosc)
        yield kontaktItem
