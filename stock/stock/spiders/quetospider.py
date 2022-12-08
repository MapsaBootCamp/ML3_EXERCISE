# import sys
# sys.path.append('/Users/arianzarifian/Downloads/W6-Arian/stock/stock/')
import scrapy
import pandas as pd
#import items



class QuotespiderSpider (scrapy.Spider):
    name='Quotespider'
    start_urls=['https://www.coingecko.com/']

    def parse(self,response):
        items=[]
        coins =response.css('tr')
        for coin in coins:
            item={ 'Rank':coin.xpath('.//td[2]/text()').get(),
            'Name':coin.css('span::text').get(),
            'price':coin.xpath('.//td[4]/div/div[2]/span/text()').get(),
            '24h_volume':coin.xpath('.//td[8]/span/text()').get(),
            'MKT_cap': coin.xpath('.//td[9]/span/text()').get(),
            
            }
            items.append(item)
        
        
        
        next_page=response.css('ul.pagination li a ::attr(href)')[-1].get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        x = pd.DataFrame(items, columns=['Rank','Name','price','24h_volume',
                'MKT_cap'])
        yield x.to_csv("stock.csv",mode='a',index=False)
 