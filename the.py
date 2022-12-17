import scrapy


class TheSpider(scrapy.Spider):
    name = 'the'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['http://www.theguardian.com/']

    def parse(self, response):
        re = response.css("div.fc-item__container").getall()
        for item in re:
            result = item.css(p.dcr-1b64dqh)
            yield result


            