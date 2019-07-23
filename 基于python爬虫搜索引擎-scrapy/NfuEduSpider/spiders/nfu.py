# -*- coding: utf-8 -*-
import scrapy
from NfuEduSpider.items import NfueduspiderItem
import re

class NfuSpider(scrapy.Spider):
    keyword = "教授"
    name = "nfu"
    allowed_domains = ["nfu.edu.cn"]
    start_urls = ['http://nfu.edu.cn/']


    def start_requests(self):
        requestList = list(super(NfuSpider, self).start_requests())
        for i in range(1,300):
            link = "http://www.nfu.edu.cn/index.php/home/article/index/cid/" + str(i)+".html"
            urlScrapyObj = scrapy.Request(link,callback=self.fromHome,meta={'link':link})
            requestList.append(urlScrapyObj)

        for i in range(1,5000):
            link = "http://www.nfu.edu.cn/index.php/home/article/search_detail/id/" + str(i)+".html"
            urlScrapyObj = scrapy.Request(link,callback=self.fromDetail,meta={'link':link})
            requestList.append(urlScrapyObj)
        for i in range(1,30):
            link = "http://www.nfu.edu.cn/index.php/home/article/search/keyword/"+self.keyword+"/p/"+str(i)+".html"
            urlScrapyObj = scrapy.Request(link,callback=self.fromSearch, meta={'link':link})
            requestList.append(urlScrapyObj)

        return requestList

    def fromHome(self, response):
        html = response.xpath('/html/body/div[4]/div/div[2]').extract()[0]
        if self.keyword in html:
            item = NfueduspiderItem()
            title = str(response.xpath('/html/head/title/text()').extract()[0]).strip()
            item['link'] = response.meta['link']
            item['title'] = title
            item['num'] = html.count(self.keyword)
            yield item

    def fromDetail(self,response):
        html = response.xpath('/html/body/div[4]/div/div/div[2]').extract()[0]
        if self.keyword in html:
            item = NfueduspiderItem()
            title = str(response.xpath('/html/head/title/text()').extract()[0]).strip()
            time = str(response.xpath('/html/body/div[4]/div/div/div[2]/p[1]/text()').extract()[0]).strip()
            timeReg = re.compile("\d+-\d+-\d+").findall(time)
            item['time'] = timeReg[0]
            item['link'] = response.meta['link']
            item['title'] = title
            item['num'] = html.count(self.keyword)
            yield item

    def fromSearch(self,response):
        html = str(response.xpath('/html/body/div[4]/div/div/div[2]').extract()[0])
        if self.keyword in html:
            item = NfueduspiderItem()
            title = str(response.xpath('/html/head/title/text()').extract()[0]).strip()
            item['link'] = response.meta['link']
            item['title'] = title
            item['num'] = html.count(self.keyword)
            print("ok",item)

            yield item


