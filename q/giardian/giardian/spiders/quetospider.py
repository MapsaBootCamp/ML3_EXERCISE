# import sys
# sys.path.append('/Users/arianzarifian/Downloads/W6-Arian/stock/stock/')
import scrapy
import pandas as pd
#import items



class QuotespiderSpider (scrapy.Spider):
    name='Quotespider'
    start_urls=['https://www.theguardian.com/theguardian/series/the-quiz-thomas-eaton']
    
    
    def parse2 (self,response):
        items=[]
        Quastions=response.xpath('/html/body/main/article/div/div/div[6]/div/div[1]/div/p[1]')
        Quastion=Quastions.xpath('.//text()').getall()
        Answers=response.xpath('/html/body/main/article/div/div/div[6]/div/div[1]/div/p[2]')
        Answer=Answers.xpath('.//text()').getall()
        numbers=len(Answer)-1
        for i in range (0,numbers):
            
            
            item={
                'Quastions':Quastion[i],
                'Answers':Answer[i]

            }
            items.append(item)
        
        
        
        
        x = pd.DataFrame(items, columns=['Quastions','Answers'])
        x.to_csv("gurdian.csv",mode='a',index=False) 

            
    
        
            


       
       
      
                
        


    def parse(self,response):
        
        titles =response.css('section')
        for title in titles:
            
            link=title.xpath('.//div/div/div/ul/li/div/div/a/@href').get()

            
            try:
                yield response.follow(link, callback=self.parse2)
            except:
                continue
        
        next_page=response.css('a.button button--small button--tertiary pagination__action   ::attr(href)')[-1].get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        
 