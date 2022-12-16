import scrapy

class ExamSpider(scrapy.Spider):
    name = 'exam'
    start_urls = ["https://www.theguardian.com/lifeandstyle/2022/dec/10/which-fellow-dystopian-taught-george-orwell-at-eton-the-saturday-quiz"]

    def parse(self, response):
        quiz = response.css('div p.dcr-18sg7f2')
        for row in range(2):
            myfile = {

            "questions" : quiz[0].extract(),
            "answers" : quiz[1].extract()
            }

            yield myfile

