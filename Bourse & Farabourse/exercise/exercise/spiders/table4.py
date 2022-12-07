#بازار نقدی بورس و فرابورس در یک نگاه دارای ادرس کلاس یکسان هستند و هردو در یک جدول ذخیره شده اند
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
        for row in response.xpath('//*[@class="box1 blue tbl z1_4 h210"]//tbody//tr'):
            table1={
            'ستون یک': row.xpath('td[1]//text()').extract(),
             'ستون دو': row.xpath('td[2]//text()').extract(),
            }

            yield table1

#Export csv----------->scrapy crawl bourse -o table4.csv