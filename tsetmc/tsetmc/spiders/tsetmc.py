import scrapy
class TsetmcSpider(scrapy.Spider):
    name = 'tsetmc'
    start_urls = ["http://www.tsetmc.com/Loader.aspx?ParTree=15"]

    def parse(self, response):
        shakhes = response.css("div div.silver.z3_4 .content:: text")
        for row in range(7):
            table1 = {
            "انتشار": shakhes[0].extract(),
            " مقدار": shakhes[1].extract(),
            "تغییر":shakhes[2].extract(),
            "درصد":shakhes[3].extract(),
            "بیشترین":shakhes[4].extract(),
            "کمترین":shakhes[5].extract()
            }
            yield table1
        portarakonesh1 =response.css('div div .silver+ .z3_4 :: text')
        for row in range(7):
            table2 = {
            "قیمت پایانی": portarakonesh1[0].extract(),
            "آخرین معامله":portarakonesh1[1].extract(),
            "کمترین ":portarakonesh1[2].extract(),
            "بیشترین":portarakonesh1[3].extract(),
            "تعداد":portarakonesh1[4].extract(),
            "حجم":portarakonesh1[5].extract(),
            "ارزش":portarakonesh1[6].extract()
             }
            yield table2
        portarakonesh2=response.css('div div .blue+ .green .content :: text')
        for row in range(7):
            table3 = {
                "قیمت پایانی": portarakonesh2[0].extract(),
                "آخرین معامله": portarakonesh2[1].extract(),
                "کمترین ": portarakonesh2[2].extract(),
                "بیشترین": portarakonesh2[3].extract(),
                "تعداد": portarakonesh2[4].extract(),
                "حجم": portarakonesh2[5].extract(),
                "ارزش": portarakonesh2[6].extract()
            }
            yield table3
        tasirshakhes1 =response.css('div div .green+ .h210::text')
        for row in range(7):
            table4 ={
                "نماد":tasirshakhes1[0].extract(),
             "قیمت پایانی":tasirshakhes1[1].extract(),
             "تاثیر":tasirshakhes1[2].extract()
            }
            yield table4

        tasirshakhes2 = response.css("div div .silver.z1_4 .content:: text")
        for row in range(7):
            table5 = {
              "نماد": tasirshakhes2[0].extract(),
             "قیمت پایانی": tasirshakhes2[1].extract(),
             "تاثیر": tasirshakhes2[2].extract()
            }
            yield table5




