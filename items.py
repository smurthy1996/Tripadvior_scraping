# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ScrapingTestingItem(scrapy.Item):
	reviews = Field()
	subjects = Field()
	stars = Field()
	names = Field()
	location = Field()
	date = Field()
	comments = Field()
	


