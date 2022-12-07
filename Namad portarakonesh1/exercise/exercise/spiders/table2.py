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
        for row in response.xpath('//*[@class="box1 white tbl z4_4 h210"]//tbody//tr'):
            table1={
            'نماد': row.xpath('td[1]//text()').extract(),
                'قیمت پایانی': row.xpath('td[2]//text()').extract(),
             'آخرین معامله': row.xpath('td[3]//text()').extract(),
            'کمترین': row.xpath('td[4]//text()').extract(),
            'بیشترین': row.xpath('td[5]//text()').extract(),
            'تعداد ': row.xpath('td[6]//text()').extract(),
            'حجم': row.xpath('td[7]//text()').extract(),
            'ارزش': row.xpath('td[8]//text()').extract(),
            }
            yield table1
#Export csv----------->scrapy crawl bourse -o table2.csv