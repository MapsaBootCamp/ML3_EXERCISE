import scrapy
from ..items import spiderItem




class QuizSpider(scrapy.Spider):
    name = 'quiz'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['https://www.theguardian.com/theguardian/series/the-quiz-thomas-eaton']


    def parse(self, response):
        # print(111111111111111111111111111111111111111111111111111111)
        try:
            mystr= response.xpath("//h3[@class='fc-item__title']//span[@class='js-headline-text']//text()").getall()
            # print(mystr)
            item=spiderItem()
            item['name']= mystr
            yield item

        except:
            print('error-----------------------------------------')
        # print(44)
        nextpage = response.xpath("//a[@class='button button--small button--tertiary pagination__action  ']")[-1].attrib['href']
        # pn=nextpage[-1]
        # print(2222222,pn, nextpage, 1111111111111111111111)
        # print(55)
        # if int(int(pn)>3):
        #     nextpage =response.xpath("//a[@class='button button--small button--tertiary pagination__action  ']")[0].attrib['href']
        #     count += 1
        #     print((count))
        # print(2222222,pn, nextpage, 1111111111111111111111)

        try:

            if nextpage:
                yield response.follow(nextpage, callback=self.parse)

        except:
            print('error--------------------------------------------------------------')



