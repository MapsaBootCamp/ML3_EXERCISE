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
        for row in response.xpath('//*[@class="box1 white tbl z3_4 h210"]//tbody//tr'):
            table1={
            'شاخص': row.xpath('td[1]//text()').extract(),
            'انتشار': row.xpath('td[2]//text()').extract(),
            'مقدار': row.xpath('td[3]//text()').extract(),
            'تغییر': row.xpath('td[4]//text()').extract(),
            'درصد': row.xpath('td[5]//text()').extract(),
            'بیشترین': row.xpath('td[6]//text()').extract(),
            'کمترین': row.xpath('td[7]//text()').extract(),
            }

            yield table1

#Export csv----------->scrapy crawl bourse -o table1.csv