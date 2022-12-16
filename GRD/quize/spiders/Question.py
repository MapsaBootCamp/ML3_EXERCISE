import scrapy


class QuestionSpider(scrapy.Spider):
    name = 'Question'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['https://www.theguardian.com/theguardian/series/the-quiz-thomas-eaton']
   
    def parse(self, response):
        Question_Page=response.xpath("//div[@class='fc-item__container']")
        for item in Question_Page:
            link=item.xpath(".//a/@href").get()
            if link:
                request=scrapy.Request(link,callback=self.parse_page_detail)
                yield request
        next_page=response.xpath("//div[@class='pagination__list']/a/@href")[-1].get()
        if next_page:
            yield response.follow(next_page,self.parse)
    def parse_page_detail(self,response):
        question_answer=response.xpath("//p[@class='dcr-1b64dqh']/text()").getall()
        yield {'quiz_content': question_answer}
Footer
