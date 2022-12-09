import scrapy
from ..items import BoorsItem
import pandas as pd
df=pd.DataFrame(columns=['shakhes', 'enteshar', 'meghdar', 'taghir', 'darsad', 'bishtarin' ,'kamtarin'])
print(df)

class BoorspiderSpider(scrapy.Spider):
    name = 'boorspider'
    allowed_domains = ['www.tsetmc.com']
    start_urls = ['http://www.tsetmc.com/Loader.aspx?ParTree=15']

    # response.css('div.ltr').get()

    def parse(self, response):

        table= response.xpath("//table[@class='table1']")[3]
        print('11111111111111111111', table, '111111111111111')
        for row in range(1,7):
            # for col in range(1, 7):
            print(22222222222222222222222222, row, 222222222222222222222222222)
            shakhes = table.xpath(f'.//tr[{row}]/td[1]//text()').get()
            enteshar = table.xpath(f'.//tr[{row}]/td[2]//text()').get()
            meghdar = table.xpath(f'.//tr[{row}]/td[3]//text()').get()
            taghir = table.xpath(f'.//tr[{row}]/td[4]//text()').get()
            darsad = table.xpath(f'.//tr[{row}]/td[5]//text()').get()
            bishtarin = table.xpath(f'.//tr[{row}]/td[6]//text()').get()
            kamtarin = table.xpath(f'.//tr[{row}]/td[7]//text()').get()
            df.loc[row]=[shakhes, enteshar,meghdar,taghir ,darsad ,bishtarin, kamtarin ]
            print(22222222222222222222222222, df, 222222222222222222222222222)

            mydata = BoorsItem(kamtarin=kamtarin, bishtarin=bishtarin ,darsad=darsad, taghir=taghir, meghdar=meghdar, enteshar=enteshar, shakhes=shakhes)
            yield mydata

        print(111111111111111111)
        print(mydata)
        # df.to_csv('2.csv')
