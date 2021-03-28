import json
import scrapy

from datetime import datetime


class PrzetargiSpider(scrapy.Spider):
    name = "przetargi"
    start_urls = ['http://www.bip.lubianka.lo.pl/?app=przetargi']

    def parse(self, response):
        linki = response.css('span a::attr(href)').getall()
        aktualne_przetargi = linki[0]
        wtoku_przetargi = linki[1]
        rozstrzygniete_przetargi = linki[2]
        uniewaznione_przetargi = linki[3]

        if aktualne_przetargi is not None:
            aktualne_przetargi = response.urljoin(aktualne_przetargi)
            yield scrapy.Request(aktualne_przetargi, callback=self.type_parse)

        if wtoku_przetargi is not None:
            wtoku_przetargi = response.urljoin(wtoku_przetargi)
            yield scrapy.Request(wtoku_przetargi, callback=self.type_parse)

        if rozstrzygniete_przetargi is not None:
            rozstrzygniete_przetargi = response.urljoin(rozstrzygniete_przetargi)
            yield scrapy.Request(rozstrzygniete_przetargi, callback=self.type_parse)

        if uniewaznione_przetargi is not None:
            uniewaznione_przetargi = response.urljoin(uniewaznione_przetargi)
            yield scrapy.Request(uniewaznione_przetargi, callback=self.type_parse)

    def type_parse(self, response):
        for link in response.css('td.men a::attr(href)'):
            yield response.follow(link, callback=self.article_parse)

        for lata in response.css('a.men::attr(href)'):
            yield response.follow(lata, callback=self.type_parse)

        next_page = response.css('td.text_normal.w-33.ta-right a::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.type_parse)

    def article_parse(self, response):
        data = {
            'title': response.css('title::text').get(),
            'date': datetime.now().strftime("%d/%m/%y %H:%M"),
            'cont_art': response.css('strong::text').getall(),
            'source': response.request.url,
        }
        wybor = response.request.url[-1]

        if wybor == '1':
            nazwa = "aktualne.json"
        elif wybor == '2':
            nazwa = "w_toku.json"
        elif wybor == '3':
            nazwa = "rozstrzygniete.json"
        elif wybor == '4':
            nazwa = "uniewaznione.json"
        else:
            nazwa = "trash.json"

        with open(nazwa, "a") as filee:
            json.dump(data,filee)

