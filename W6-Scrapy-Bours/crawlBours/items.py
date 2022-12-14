# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class CrawlboursTable2(scrapy.Item):
    # define the fields for your item here like:
    Shakhes = scrapy.Field()
    Enteshar=scrapy.Field()
    Meghdar=scrapy.Field()
    Taghir=scrapy.Field()
    Darsad=scrapy.Field()
    Bishtarin=scrapy.Field()
    Kamtarin=scrapy.Field()

