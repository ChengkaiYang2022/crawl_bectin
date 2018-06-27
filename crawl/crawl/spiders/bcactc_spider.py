# -*- coding: utf-8 -*-

import scrapy
import regex as rex
import json
from crawl.items import CrawlItem
import requests as re
class BcactcSpider(scrapy.Spider):
    name = "bcactc"

    def start_requests(self):
        urls = [
            "http://www.bcactc.com/home/gcxx/now_kcsjzbgs.aspx",  # 勘察设计
            "http://www.bcactc.com/home/gcxx/now_sgzbgs.aspx",  # 施工
            "http://www.bcactc.com/home/gcxx/now_jlzbgs.aspx",  # 监理
            "http://www.bcactc.com/home/gcxx/now_zyzbgs.aspx",  # 专业
            "http://www.bcactc.com/home/gcxx/now_clsbzbgs.aspx",  # 材料设备
            "http://www.bcactc.com/home/gcxx/now_lwzbgs.aspx",  # 劳务
            "http://www.bcactc.com/home/gcxx/now_tdzbgs.aspx",  # 铁路
            "http://www.bcactc.com/home/gcxx/now_ylzbgs.aspx",  # 园林
            "http://www.bcactc.com/home/gcxx/now_mhzbgs.aspx",  # 民航
            "http://www.bcactc.com/home/gcxx/now_jdzbgs.aspx"  # 军队
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)
        url_pre =u'http://www.bcactc.com/home/gcxx/'
        links = response.xpath("//a[@target='_blank']/@href").extract()
        for i in links:
            real_link = url_pre+i
            yield scrapy.Request(url=real_link,callback = self.parse_page)
        print(response)

    def get_real_pdf_link(self, project_id):
        js_pdf_link_pre = u"http://file.bcactc.com/FileInterface/Filelist.ashx?projectid={0}&node={1}".format(project_id,
                                                                                                              'zbgs')
        a = str(re.get(js_pdf_link_pre).text)
        b = rex.search(r"{.+}",a)
        if b is None:
            return "无pdf"
        else:
            result = b.group()
            dict = json.loads(b.group())
            return  u"http://file.bcactc.com/FileInterface/FileRead.ashx?filename={0}".format(dict["filename"])

    def parse_page(self, response):
        item = CrawlItem()
        try:
            project_id = response.xpath("//span[@id='gcbh']").xpath('string(.)').extract_first()
            title = response.xpath("//span[@id='gcmc']").xpath('string(.)').extract_first()
            company = response.xpath("//span[@id='jsdwmc']").xpath('string(.)').extract_first()
            date = response.xpath("//span[@id='zbsj']").xpath('string(.)').extract_first()

            project_link = response.url

            item["project_id"] = project_id
            item["title"] = title
            item["company"] = company
            item["date"] = date
            item["project_link"] = project_link
            item["pdf_real_link"] = self.get_real_pdf_link(project_id)

        except Exception as e:
            print e
        print(response)
        yield item

