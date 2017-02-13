# -*- coding: utf-8 -*-
import scrapy
import time
from Recruit.items import RecruitItem
from scrapy.selector import Selector
from selenium import webdriver

class RecruitSpider(scrapy.Spider):
 
	#spider 이름
	name = "recruitCrawler"
	 
	def __init__(self):
		self.driver = webdriver.Chrome("/Users/thyun.ahn/chromedriver")
	 
	
	#-- url list
	 
	#시작주소를 리스트 형태로 추가할 수 있음
	#start_urls = []
	
	#콜백함수를 지정할 수 있으며, 로그인등의 로직을 추가할 수 있음
	def start_requests(self):

		yield scrapy.Request("https://recruit.daou.co.kr/?S_DSCLASS=biz.rem.apply.applicant.Apply_list&S_DSMETHOD=search01&S_PAGE_NO=1&S_PAGE_CNT=1&S_FORWARD=xsheetResultXML    &S_MENU_TYPE=2&S_TOP_TYPE=2&S_ANN_TYPE=&S_ANN_SEQ_NO=&indexLeft_menu2=0&S_C_CD=10&S_RE_NO=&S_APPL_NO=&S_WEB_TYPE=", self.parse_daou)
		# yield scrapy.Request("https://recruit.daou.co.kr" ,self.parse_daou)
		 
		
	def parse_daou(self, response):
		print ("hello world!!!")
		self.driver.get(response.url)
		time.sleep(5)

		html = self.driver.find_element_by_xpath('//*').get_attribute('outerHTML')
		
		selector = Selector(text=html)

		rows = selector.xpath("//tbody[@id='listBody']/tr/td[@class='alignL']/a")
		for sel in rows:
			#item class 명
			item = RecruitItem()
			item['source'] = "다우기술"
			item['title']  = sel.xpath("text()").extract()[0]
			print(item['title'])
			yield item
