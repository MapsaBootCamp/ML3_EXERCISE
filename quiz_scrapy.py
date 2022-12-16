import scrapy


class QuizScrapySpider(scrapy.Spider):
    name = 'quiz_scrapy'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['http://www.theguardian.com/']

    def parse(self, response):
        items1 = []
        table1 = response.xpath('//div/a[@class="fc-item__link"]/text()').get()
        for row1 in table1:
            item1 = {
                'question': row1.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row1.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items1.append(item1)

        items2 = []
        table2 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row2 in table2:
            item2 = {
                'question': row2.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row2.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items2.append(item2)

        items3 = []
        table3 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row3 in table3:
            item3 = {
                'question': row3.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row3.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items3.append(item3)

        items4 = []
        table4 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row4 in table4:
            item4 = {
                'question': row4.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row4.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items4.append(item4)

        items5 = []
        table5 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row5 in table5:
            item5 = {
                'question': row5.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row5.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items5.append(item5)

        items6 = []
        table6 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row6 in table6:
            item6 = {
                'question': row6.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row6.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items6.append(item6)

        items7 = []
        table7 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row7 in table7:
            item7 = {
                'question': row7.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row7.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items7.append(item7)

        items8 = []
        table8 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row8 in table8:
            item8 = {
                'question': row8.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row8.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items8.append(item8)

        items9 = []
        table9 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row9 in table9:
            item9 = {
                'question': row9.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row9.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items9.append(item9)

        items10 = []
        table10 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row10 in table10:
            item10 = {
                'question': row10.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row10.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items10.append(item10)

        items11 = []
        table11 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row11 in table11:
            item11 = {
                'question': row11.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row11.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items11.append(item11)

        items12 = []
        table12 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row12 in table12:
            item12 = {
                'question': row12.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row12.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items12.append(item12)

        items13 = []
        table13 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row13 in table13:
            item13 = {
                'question': row13.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row13.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items13.append(item13)

        items14 = []
        table14 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row14 in table14:
            item14 = {
                'question': row14.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row14.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items14.append(item14)

        items15 = []
        table15 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row15 in table15:
            item15 = {
                'question': row15.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row15.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items2.append(item15)

        items16 = []
        table16 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row16 in table16:
            item16 = {
                'question': row16.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row16.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items16.append(item16)

        items17 = []
        table17 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row17 in table17:
            item17 = {
                'question': row17.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row17.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items17.append(item17)

        items18 = []
        table18 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row18 in table18:
            item18 = {
                'question': row18.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row18.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items18.append(item18)

        items19 = []
        table19 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row19 in table19:
            item19 = {
                'question': row19.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row19.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items19.append(item19)

        items20 = []
        table20 = response.xpath('//div/a[@class="u-faux-block-link__overlay js-headline-text"]/text()').get()
        for row20 in table20:
            item20 = {
                'question': row20.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall(),
                'answer': row20.xpath('//div/p[@class="dcr-1b64dqh"]/text()').getall()
            }
            items20.append(item20)

        yield {1: items1, 2: items2, 3: items3, 4: items4, 5: items5, 6: items6, 7: items7, 8: items8, 9: items9,
               10: items10, 11: items11, 12: items12, 13: items13, 14: items14, 15: items15, 16: items16, 17: items17,
               18: items18,
               19: items19, 20: items20}
        