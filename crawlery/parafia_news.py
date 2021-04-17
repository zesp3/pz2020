import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = ['https://parafiabierzglowo.wordpress.com/page1']



    # znalezienie najnowszego postu
    def parse(self, response):

        first = response.xpath('//article').css('.entry-content').css('a::attr(href)').get()
        yield response.follow(first, self.parse_next)

    #przetwarzanie pierwszego i kolejnych postów
    def parse_next(self, response):

        title = response.css('.entry-title ::text').get()
        date = response.css('.entry-date ::text').get()
        date2 = response.css('.entry-date').attrib['datetime']
        # content = response.css('.entry-content').css('p').getall()
        content = response.css('.entry-content').css('p::text').getall()
        yield {
            'title': title,
            'date': date,
            'date2': date2,
            'content': content,
        }

        next_post = response.css('div.nav-previous a::attr("href")').get()
        if next_post is not None:
            yield response.follow(next_post, self.parse_next)
