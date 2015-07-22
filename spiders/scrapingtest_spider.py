from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapingtest.items import ScrapingTestingItem
from collections import OrderedDict
import json
from scrapy.selector.lxmlsel import HtmlXPathSelector
import csv







class scrapingtestspider(Spider):
    name = "scrapytesting"
    allowed_domains = ["tripadvisor.in"]
    base_uri = ["tripadvisor.in"]
    start_urls = [

"http://www.tripadvisor.in/Hotel_Review-g1009352-d1173080-Reviews-Yercaud_Rock_Perch_A_Sterling_Holidays_Resort-Yercaud_Tamil_Nadu.html"]
    


    def parse(self, response):
        item = ScrapingTestingItem()
        sel = Selector(response)
        sites = sel.xpath('//a[contains(text(), "Next")]/@href').extract()
##        item['comments'] = ['False' for i in range(10)]

        item['reviews'] = sel.xpath('//div[@class="col2of2"]//p[@class="partial_entry"]/text()').extract()
        item['subjects'] = sel.xpath('//span[@class="noQuotes"]/text()').extract()
        item['stars'] = sel.xpath('//*[@class="rating reviewItemInline"]//img/@alt').extract()
        item['names'] = sel.xpath('//*[@class="username mo"]/span/text()').extract()
        item['location'] = sel.xpath('//*[@class="location"]/text()').extract()
        item['date'] = sel.xpath('//*[@class="ratingDate relativeDate"]/@title').extract()
        item['date'] += sel.xpath('//div[@class="col2of2"]//span[@class="ratingDate"]/text()').extract()
##
##        temp_id_rev =  sel.xpath('//div[@class="reviewSelector  " or @class="reviewSelectortrack_back"]/@id').extract()
##        temp_id = sel.xpath('//div[@class="col2of2"]//p[2]//span/@id').extract()
##        
##        for f  in range(len(temp_id_rev)):
##            temp_id_rev[f] = temp_id_rev[f][7:].strip()
##
##        for k in range(len(temp_id)):
##            temp_id[k] = temp_id[k][9:].strip()
##        print len(temp_xpath)
##        for u in range(len(temp_id)):
##            item['comments'].insert(temp_id_rev.index(temp_id[u]),'True')
        
        startingrange = len(sel.xpath('//*[@class="ratingDate relativeDate"]/@title').extract())
        for j in range(startingrange,len(item['date'])):
            item['date'][j] = item['date'][j][9:].strip()

        for i in range(len(item['stars'])):
            item['stars'][i] = item['stars'][i][:1].strip()

        while "\n" in item['reviews']: item['reviews'].remove("\n")
        while "\n" in item['subjects']: item['subjects'].remove("\n")
##        while "\n" in item['comments']: item['comments'].remove("\n")

        


        yield item
        
        if(sites and len(sites) > 0):
            for site in sites:
                yield Request(url="http://tripadvisor.in" + site, callback=self.parse)        


