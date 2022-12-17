import scrapy
from ..items import spiderItem




class QuizSpider(scrapy.Spider):
    name = 'quiz'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['https://www.theguardian.com/theguardian/series/the-quiz-thomas-eaton']


    def parse(self, response):
        
        try:
            mystr= response.xpath("//h3[@class='fc-item__title']//span[@class='js-headline-text']//text()").getall()
            
            item=spiderItem()
            item['name']= mystr
            yield item

        except:
            print('0')
        
        nextpage = response.xpath("//a[@class='button button--small button--tertiary pagination__action  ']")[-1].attrib['href']


        try:

            if nextpage:
                yield response.follow(nextpage, callback=self.parse)

        except:
            print('0')



