from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
	executable_path='../webdriver/chromedriver'
)

url = 'http://ecolife.me.go.kr/ecolife/chmstryProduct/chmstryProductIndex?prdCd=01&page=6'
driver.get(url)

url = 'http://ecolife.me.go.kr/ecolife/chmstryProduct/chmstryProductIndex?prdCd=01&page=6'
driver.get(url)

def parser(pageStr):
	bsObj = BeautifulSoup(pageStr, 'html.parser')

	table = bsObj.find('table', {'class': 'table table-striped2'})
	aEle = bsObj.select('table.table-striped2 > tbody > tr > td > a')
	# print(type(aEle))
	# trs = table.findAll('tr')
	# print(trs[0])
	return list([a.text for a in aEle])

pageString = driver.page_source
print(parser(pageString))
