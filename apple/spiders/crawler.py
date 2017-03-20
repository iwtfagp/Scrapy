import scrapy
from bs4 import BeautifulSoup
from apple.items import AppleItem

class AppleCrawler(scrapy.Spider):
	name = 'apple'
	start_urls = ['http://www.appledaily.com.tw/realtimenews/section/new/']
	def parse(self, response):
	    res = BeautifulSoup(response.body)
	    domain = 'http://www.appledaily.com.tw/'
	    for news in res.select('.rtddt'):
#	    	print news.select('h1')[0].text
#		print domain + news.select('a')[0]['href']
		yield scrapy.Request(domain + news.select('a')[0]['href'], self.parse_detail)

	def parse_detail(self, response):
	    res = BeautifulSoup(response.body)
            appleitem = AppleItem();
            appleitem['title'] = res.select('#h1')[0].text
            appleitem['content'] = res.select('.trans')[0].text
            appleitem['time'] = res.select('.gggs time')[0].text
#	    print res.select('#h1')[0].text
            return appleitem

