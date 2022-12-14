import scrapy
# from ..items import CrawlboursItem


class Table1Spider(scrapy.Spider):
    name = 'Table1'
    allowed_domains = ['tsetmc.com']
    start_urls = ['http://tsetmc.com/loader.aspx?partree=15']

    def parse(self, response):
        
        Bours_Tables=response.xpath("//div[@class='rainbow_global_elm box1 white zFull']")
        Table1 = Bours_Tables.xpath(".//div[@class='rainbow_tse_elm content']").xpath(".//div[@class='box1 blue tbl z1_4 h210']")
        maintitle=Table1.xpath(".//div[@class='header']/text()").get()
        # yield {'maintitle':maintitle}
        data=Table1.xpath('.//tr')
        for item in data:
            title=item.xpath('.//td[1]/text()').get()
            content=item.xpath('(.//td[2]|.//td[2]/div)/text()').get() # بعضی هاش تگ دیو داره داخلش پس از عملگر منظقی یا برای بررسی دو حالت استفاده می کنیم
            yield {'title': title,
                    'content': content}
                    
        # Bours_Tables=response.css(".rainbow_global_elm.box1.white.zFull")
        # # print(Bours_Tables)
        # # for item in Bours_Tables:
        # Table1 = Bours_Tables.css(".rainbow_tse_elm.content").css('.box1.blue.tbl.z1_4.h210')
        # Table2=Bours_Tables.css('.box1.silver.tbl.z3_4.h210')
        # Table3=Bours_Tables.css('.box1.silver.tbl.z1_4.h210')
        # Table4=Bours_Tables.css('.box1.green.tbl.z3_4.h210')
        # Table5=Bours_Tables.css('.box1.blue.tbl.z1_4.h210')
        # Table6=Bours_Tables.css('.box1.green.tbl.z3_4.h210')
        # Table7=Bours_Tables.css('.box1.silver.tbl.z1_4.h210')

        # maintitle=Table1.css('.header::text').get()
        # print(maintitle)
        # yield {'title': maintitle}
        # data=Table1.css('tr')
        # for item in data:
        #     title=item.css('.//tr/text()')[0].get()
        #     content=item.css('td')[1].get() #بعضی هاش تگ دیو داره داخلش
        #     print(title)
        #     print(content)
        #     yield {'title': title,
        #             'content': content}
