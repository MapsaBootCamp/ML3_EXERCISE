import scrapy
from ..items import CrawlboursTable2


class Table2Spider(scrapy.Spider):
    name = 'Table2'
    allowed_domains = ['tsetmc.com']
    start_urls = ['http://tsetmc.com/loader.aspx?partree=15']

# xpath(".//div[@class='rainbow_tse_elm content']")
    def parse(self, response):
            # Bours_Tables=response.xpath("//div[@class='rainbow_global_elm box1 white zFull']")
            # Table2 = Bours_Tables.xpath(".//div[@class='rainbow_tse_elm content']").xpath(".//div[@class='box1 silver tbl z3_4 h210']")
            
        Table2=response.xpath("//div[@class='box1 white tbl z3_4 h210']")
        maintitle=Table2.xpath(".//div[@class='header pointer']/text()").get()
        print(maintitle)
        # yield {'maintitle':maintitle}
        data = Table2.xpath('.//tbody/tr')
        print(data)
        # print(data[2].xpath(".//td/a/text()").get())
        Table2_Column=CrawlboursTable2()
        for item in data:
            Table2_Column['Shakhes']=item.xpath(".//td[1]/a/text()").get()
            Table2_Column['Enteshar']=item.xpath(".//td[2]/text()").get()
            Table2_Column['Meghdar']=item.xpath(".//td[3]/text()").get()
            Table2_Column['Taghir']=item.xpath(".//td[4]/div/text()").get()
            Table2_Column['Darsad']=item.xpath(".//td[5]/div/text()").get()
            Table2_Column['Bishtarin']=item.xpath(".//td[6]/text()").get()
            Table2_Column['Kamtarin']=item.xpath(".//td[7]/text()").get()
            yield Table2_Column
        