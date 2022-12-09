import scrapy


class BoorsSpider(scrapy.Spider):
    name = 'boors'
    allowed_domains = ['www.tsetmc.com']
    start_urls = ['http://www.tsetmc.com/Loader.aspx?ParTree=15']

    def parse(self, response):
        items = []
        box = response.xpath('//div[@class="rainbow_global_elm box1 white zFull"]/text()')
        for item1_ in box:
            table1 = item1_.xpath('//table[@class="table1"]/text()')
            for row1 in table1:
                item = {
                    'وضعیت بازار': row1.xpath('//table/tr[1]/td[2]//text()').get(),
                    'شاخص کل': row1.xpath('//table/tr[2]/td[2]//text()').get(),
                    'هم وزن': row1.xpath('//table/tr[3]/td[2]//text()'),
                    'ارزش بازار': row1.xpath('//table/tr[4]/td[2]//text()'),
                    'اطلاعات قیمت': row1.xpath('//table/tr[5]/td[2]//text()'),
                    'تعداد معاملات': row1.xpath('//table/tr[6]/td[2]//text()'),
                    'ارزش معاملات': row1.xpath('//table/tr[7]/td[2]//text()'),
                    'حجم معاملات': row1.xpath('//table/tr[8]/td[2]//text()')
                }
                items.append(item)

            table2 = item1_.xpath('//table[@class="table1"]/text()')
            for row2 in table2:
                item1 = {
                    'شاخص كل': row2.xpath('//table/tr[1]/td[2:7]//text()'),
                    'وزني-ارزشی)': row2.xpath('//table/tr[2]/td[2:7]//text()'),
                    'شاخص كل(هم وزن)': row2.xpath('//table/tr[3]/td[2:7]//text()'),
                    'هم وزن': row2.xpath('//table/tr[4]/td[2:7]//text()'),
                    'شاخص آزاد شناور': row2.xpath('//table/tr[5]/td[2:7]//text()'),
                    'شاخص بازار اول': row2.xpath('//table/tr[6]/td[2:7]//text()'),
                    'شاخص بازار دوم': row2.xpath('//table/tr[7]/td[2:7]//text()')
                }
                items.append(item1)

            table3 = item1_.xpath('//table[@class="table1"]/text()')
            for row3 in table3:
                item3 = {
                    'ميدكو': row3.xpath('//table/tr[1]/td[2:3]//text()').get(),
                    'فارس': row3.xpath('//table/tr[2]/td[2:3]//text()').get(),
                    'وپاسار': row3.xpath('//table/tr[3]/td[2:3]//text()'),
                    'فملي': row3.xpath('//table/tr[4]/td[2:3]//text()'),
                    'فولاد': row3.xpath('//table/tr[5]/td[2:3]//text()'),
                    'شبندر': row3.xpath('//table/tr[6]/td[2:3]//text()'),
                    'خودرو': row3.xpath('//table/tr[7]/td[2:3]//text()')
                }
                items.append(item3)

            table4 = item1_.xpath('//table[@class="table1"]/text()')
            for row4 in table4:
                item4 = {
                    'خساپا - سايپا': row4.xpath('//table/tr[1]/td[2:10]//text()').get(),
                    'خودرو - ايران‌ خودرو': row4.xpath('//table/tr[2]/td[2:10]//text()').get(),
                    'خگستر - گسترش‌سرمايه‌گذاري‌ايران‌خودرو': row4.xpath('//table/tr[3]/td[2:10]//text()'),
                    'شبندر - پالايش نفت بندرعباس': row4.xpath('//table/tr[4]/td[2:10]//text()'),
                    'شپنا - پالايش نفت اصفهان': row4.xpath('//table/tr[5]/td[2:10]//text()'),
                    'شتران - پالايش نفت شستا - سرمايه گذاري تامين اجتماعي': row4.xpath(
                        '//table/tr[6]/td[2:10]//text()'),
                    'شستا - سرمايه گذاري تامين اجتماعي': row4.xpath('//table/tr[7]/td[2:10]//text()')
                }
                items.append(item4)

            table5 = item1_.xpath('//table[@class="table1"]/text()')
            for row5 in table5:
                item5 = {
                    'وضعیت بازار': row5.xpath('//table/tr[1]/td[2]//text()').get(),
                    'شاخص کل': row5.xpath('//table/tr[2]/td[2]//text()').get(),
                    'ارزش بازار اول و دوم': row5.xpath('//table/tr[3]/td[2]//text()'),
                    'ارزش بازار پایه': row5.xpath('//table/tr[4]/td[2]//text()'),
                    'اطلاعات قیمت': row5.xpath('//table/tr[5]/td[2]//text()'),
                    'تعداد معاملات': row5.xpath('//table/tr[6]/td[2]//text()'),
                    'ارزش معاملات': row5.xpath('//table/tr[7]/td[2]//text()'),
                    'حجم معاملات': row5.xpath('//table/tr[8]/td[2]//text()')
                }
                items.append(item5)

            table6 = item1_.xpath('//table[@class="table1"]/text()')
            for row6 in table6:
                item6 = {
                    'دي - بانك دي': row6.xpath('//table/tr[1]/td[1:10]//text()').get(),
                    'فتوسا - توليد و توسعه سرب روي ايرانيانو': row6.xpath('//table/tr[2]/td[2:10]//text()').get(),
                    'سمگا - گروه سرمايه گذاري ميراث فرهنگي': row6.xpath('//table/tr[3]/td[2:10]//text()'),
                    'كرمان - س. توسعه و عمران استان كرمان': row6.xpath('//table/tr[4]/td[2:10]//text()'),
                    'سبزوا - سيمان لار سبزوار': row6.xpath('//table/tr[5]/td[2:10]//text()'),
                    'فرابورس - فرابورس ايران': row6.xpath('//table/tr[6]/td[2:10]//text()'),
                    'فگستر - گسترش صنايع روي ايرانيان': row6.xpath('//table/tr[6]/td[2:10]//text()')
                }
                items.append(item6)

            table7 = item1_.xpath('//table[@class="table1"]/text()')
            for row7 in table7:
                item7 = {
                    'آريا': row7.xpath('//table/tr[1]/td[2:3]//text()').get(),
                    'زاگرس': row7.xpath('//table/tr[2]/td[2:3]//text()').get(),
                    'بپاس': row7.xpath('//table/tr[3]/td[2:3]//text()'),
                    'غصينو': row7.xpath('//table/tr[4]/td[2:3]//text()'),
                    'شراز': row7.xpath('//table/tr[5]/td[2:3]//text()'),
                    'شاوان': row7.xpath('//table/tr[6]/td[2:3]//text()'),
                    'صبا': row7.xpath('//table/tr[7]/td[2:3]//text()')
                }
                items.append(item7)

            yield items

        

#       for item in box:
#           title = item.css('.header::text').get()
#           table = item.xpath('//div[@class="content"]/text()')
#          for item1 in table:
#              table1 = item1.xpath('//div[@class="box1 blue tbl z1_4 h210"]/text()')
#             for item2 in table1:
#                title1 = item2.css('.header::text').get()
#               body1 = item2.xpath('//*[@class="table1"]/table//tr').extract()
#
#               table2 = item1.xpath('//*[@class="box1 silver tbl z3_4 h210"]/div//tr')
#              for item3 in table2:
#                 title2 = item3.css('.header pointer::text').get()
#                body2 = item3.xpath('//*[@class="table1"]/table//tr').extract()
#
#               table3 = item1.xpath('//*[@class="box1 silver tbl z1_4 h210"]/div//tr')
#              for item4 in table3:
#                 title3 = item4.css('.header pointer::text').get()
#                body3 = item4.xpath('//*[@class="table1"]/table//tr').extract()
#
#               table4 = item1.xpath('//*[@class="box1 green tbl z3_4 h210"]/div//tr')
#              for item5 in table4:
#                 title4 = item5.css('.header pointer').get()
#                body4 = item5.xpath('//*[@class="table1"]/table//tr').extract()
#
#           title_ = item.css('.header::text').get()
#          table_ = item.xpath('//div[@class="content"]/text()')
#         for item1_ in table_:
#            table1_ = item1_.xpath('//div[@class="box1 blue tbl z1_4 h210"]/text()')
#           for item2_ in table1_:
#              title1_ = item2_.css('.header::text').get()
#             body1_ = item2_.xpath('//*[@class="table1"]/table//tr').extract()
#
#               table2_ = item1_.xpath('//div[@class="box1 green tbl z3_4 h210""]/text()')
#              for item3_ in table2_:
#                 title2_ = item3_.css('.header pointer::text').get()
#                body2_ = item3_.xpath('//*[@class="table1"]/table//tr').extract()
#
#               table3_ = item1_.xpath('//div[@class="box1 silver tbl z1_4 h210"]/text()')
#              for item4_ in table3_:
#                 title3_ = item4_.css('.header pointer::text').get()
#                body3_ = item4_.xpath('//*[@class="table1"]/table//tr').extract()
