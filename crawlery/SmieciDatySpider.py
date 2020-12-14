import scrapy
import datetime


class SmieciDatySpider(scrapy.Spider):
    name = "daty"
    start_urls = [
        "https://www.lubianka.pl/"
    ]

    def parse(self, response):
        month = [
            "stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia",
            "września", "października", "listopada", "grudnia",
        ]
        month1 = [
            "styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień",
            "wrzesień", "październik", "listopad", "grudzień",
        ]
        data1 = response.xpath('/html/body/div[2]/div[10]/div/div[2]/div[2]/div[1]/h2/strong/span/text()').re(
            r'od (.*) do')
        data2 = response.xpath('/html/body/div[2]/div[10]/div/div[2]/div[2]/div[1]/h2/strong/span/text()').re(
            r'do (.*)')
        from_date = " ".join(map(str, data1)).split(" ")
        to_date = " ".join(map(str, data2)).split(" ")
        for i in range(0, 12):
            if from_date[1] == month[i] or from_date[1] == month1[i]:
                from_date[1] = str(i + 1)
            if to_date[1] == month[i] or to_date[1] == month1[i]:
                to_date[1] = str(i + 1)
        try:
            from_datetime = datetime.datetime(int(from_date[2]), int(from_date[1]), int(from_date[0]))
        except:
            from_datetime = datetime.datetime(int(to_date[2]), int(from_date[1]), int(from_date[0]))
        try:
            to_datetime = datetime.datetime(int(to_date[2]), int(to_date[1]), int(to_date[0]))
        except:
            to_datetime = datetime.datetime(int(from_date[2]), int(to_date[1]), int(to_date[0]))
        print(from_datetime)
        print(to_datetime)
