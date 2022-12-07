#تاثیر در شاخص 1 و 2 دارای کلاس های یکسان هستند هردو را در یک جدول ذخیره کرده است
import scrapy
class Exit(scrapy.Spider):
    name='bourse'
    start_urls=['http://www.tsetmc.com/Loader.aspx?ParTree=15']

    def start_requests(self):
        urls = [
            'http://www.tsetmc.com/Loader.aspx?ParTree=15',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for row in response.xpath('//*[@class="box1 white tbl z1_4 h210"]//tbody//tr'):
            table1={
            'نماد': row.xpath('td[1]//text()').extract(),
             'قیمت پایانی': row.xpath('td[2]//text()').extract(),
            'تاثیر': row.xpath('td[3]//text()').extract(),

            }
            yield table1

#Export csv----------->scrapy crawl bourse -o table5.csv