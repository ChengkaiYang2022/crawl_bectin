# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    project_id = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    date = scrapy.Field()
    pdf_real_link =scrapy.Field()
    project_link = scrapy.Field()

    pass
