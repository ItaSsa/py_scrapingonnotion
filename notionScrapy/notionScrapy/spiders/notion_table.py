import scrapy


class NotionTableSpider(scrapy.Spider):
    name = "notion_table"
    allowed_domains = ["notion.so"]
    start_urls = ["https://www.notion.so/Cases-STAR-Matriz-de-Situa-es-STAR-15ab201f11ba81e6a843fbd85b000669"]

    def parse(self, response):
        pass
