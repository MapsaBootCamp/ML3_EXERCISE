import scrapy
from .. import items   ########## very important to access modules in upper dir

class GuardianSpiderSpider(scrapy.Spider):
    name = 'guardian_spider'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['https://www.theguardian.com/theguardian/series/the-quiz-thomas-eaton']

    def parse(self, response):
        all_quizes = response.css("section.fc-container.fc-container--tag")
        for quiz in all_quizes:
            link = quiz.css("h3 a::attr(href)").get()
            # print("*************************************************************",link)
            quiz_item = items.GuardianItem(link = link)
            if link:
                req = scrapy.Request(url = link , callback= self.get_qa)
                req.meta["itemm"] = quiz_item

                yield req


        next_page = response.css("a.button.button--small.button--tertiary.pagination__action--static::attr(href)")[-1].get()
        if next_page:
            print("PAGE NUMBERRRRRRRRRRRRRRRR : " , next_page[-5:])
            yield response.follow(next_page, callback=self.parse)




    def get_qa(self,response):
        quiz_item = response.meta["itemm"]
        section = response.css("div.article-body-commercial-selector.article-body-viewer-selector.dcr-1vqv39r")
        questions= section.css("p.dcr-1b64dqh")[0].css("p.dcr-1b64dqh ::text").getall() #returns list of questions
        answers = section.css("p.dcr-1b64dqh")[1].css("p.dcr-1b64dqh ::text").getall() # apparently the space before ::text matters. with out it inner tags are ignored

        # quiz_item.questions = "||".join(questions)  ####### DO NOT USE DOT NOTATION !!!!!!!!!
        # quiz_item.answers = "||".join(answers)
        quiz_item["questions"] = "||".join(questions) 
        quiz_item["answers"] = "||".join(answers)

        yield quiz_item


