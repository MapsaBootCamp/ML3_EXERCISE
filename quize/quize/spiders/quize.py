import scrapy
class Exit(scrapy.Spider):
    name='quize'
    start_urls=['https://www.theguardian.com/lifeandstyle/2022/dec/10/which-fellow-dystopian-taught-george-orwell-at-eton-the-saturday-quiz']
    def start_requests(self):
        urls = [
            'https://www.theguardian.com/lifeandstyle/2022/dec/10/which-fellow-dystopian-taught-george-orwell-at-eton-the-saturday-quiz',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for row in response.css('p.dcr-18sg7f2'):
            table1={

            'quize_content': row.css('p::text').extract()

            }

            yield table1

#Export csv----------->scrapy crawl quize -o quize.csv