import scrapy

class KontaktSpider(scrapy.Spider):
    name = "kontakt"
    start_urls = ['https://parafiabierzglowo.wordpress.com/kontakt']


    def parse(self, response):

        query = response.xpath('//article//p').getall()
        for q in query:

            if("contact-submit" not in str(q)):
                yield {
                    'inform': q,
                }












