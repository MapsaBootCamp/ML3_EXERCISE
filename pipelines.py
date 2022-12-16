from itemadapter import ItemAdapter


class CrawlboursPipeline:
    def process_item(self, item, spider):
        return item