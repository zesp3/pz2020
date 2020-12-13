import scrapy


class SmieciSpider(scrapy.Spider):
    name = "smieci"
    start_urls = [
        "https://www.lubianka.pl/"
    ]

    def _parse(self, response):
        for index, new_response in enumerate(response.xpath('/html/body/div[2]/div[10]/div/div[2]/div[2]//@href')):
            yield{
                "picture&PDF": self.start_urls[0] + new_response.get()
            }