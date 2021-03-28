import scrapy
from inline_requests import inline_requests


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        "https://www.lubianka.pl/9411,wszystkie-aktualnosci"
    ]

    # def start_requests(self):
    #   yield scrapy.Request(url=url, callback=self.parse)

    @inline_requests
    def parse(self, response):
        for index, quote in enumerate(response.css('li.news_box')):
            new_url = quote.css('div.news_wyswietl_wiecej a::attr(href)').get()
            try:
                next_resp: scrapy.http.Response = yield scrapy.Request(new_url)
                yield {
                    'title': quote.css('h3.system_margin0::text').get(),
                    'date': quote.css('div.news_data::text').get(),
                    'picture': self.avoidEmptyImage(quote),
                    'cont_art': self.avoidPdf(next_resp),
                    'source': new_url
                }
            except:
                yield {
                    'title': quote.css('h3.system_margin0::text').get(),
                    'date': quote.css('div.news_data::text').get(),
                    'picture': self.avoidEmptyImage(quote),
                    'cont_art': "ERROR 404",
                    'source': new_url
                }
        next_page = response.css('a.stronicowanie_nastepne::attr(href)')[1].get()
        if next_page is not None:
            next_page = response.urljoin('https://www.lubianka.pl/' + next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def avoidPdf(self, response: scrapy.http.Response):
        try:
            return response.css('div.system_anchor.obiekt_akapit').get().replace("\n", "").replace("\t", "")
        except:
            url = response.url
            return url

    def avoidEmptyImage(self, response: scrapy.http.Response):
        try:
            picture = "https://www.lubianka.pl/" + response.css("div.img_src img::attr(src)").get(),
            return picture
        except:
            return "https://www.lubianka.pl/news,obrazek,2335,wznowienie-przyjmowania-odpadow-komunalnych-do-punktu-selektywnego-zbierania-odpadow-komunalnych.png"
