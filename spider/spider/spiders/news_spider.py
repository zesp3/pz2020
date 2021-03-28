
import scrapy
import json
class NewsSpider(scrapy.Spider):
    name = "news"
    def start_requests(self):
        urls = [
        "https://www.lubianka.pl/9411,wszystkie-aktualnosci"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        with open("data_file.json", "w") as filee:
            filee.write('[')
            for index, quote in enumerate(response.css('li.news_box')):
                json.dump({
                    'title': quote.css('h3.system_margin0::text').get(),
                    'date': response.css('div.news_data::text').get(),
                    'picture': "https://www.lubianka.pl/" + response.css("div.img_src img::attr(src)").get()
                }, filee)
                if index < len(response.css('div.quote')) - 1:
                    filee.write(',')
            filee.write(']')