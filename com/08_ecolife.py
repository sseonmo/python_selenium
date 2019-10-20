from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import json
import pandas as pd
import openpyxl

driver = webdriver.Chrome(
	executable_path='../webdriver/chromedriver77'
)

def getProductInfo(tr):
	tds = tr.findAll("td")
	return {"no": tds[0].text, "name": tds[1].text, "category": tds[2].text,
			"vendor": tds[3].text, "confirmNo": tds[4].text, "licenceNo": tds[5].text}

def parser(pageString):
	bsObj = BeautifulSoup(pageString, "html.parser")
	table = bsObj.find("table", {"class": "table table-striped2"})
	tbody = table.find("tbody")
	trs = tbody.findAll("tr")
	productInfos = []
	for tr in trs:
		productInfo = getProductInfo(tr)
		productInfos.append(productInfo)
	return productInfos

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()

url = 'http://ecolife.me.go.kr/ecolife/sntryAid/index?page=6'
driver.get(url)

def getInfos(pageNo):
	url = 'http://ecolife.me.go.kr/ecolife/sntryAid/index?page={}'.format(pageNo)
	driver.get(url)
	pageString = driver.page_source
	return parser(pageString)

result = []
for page in range(1, 10 + 1):
	result = result + getInfos(page)

df = pd.DataFrame(data=result)
print(df.count())
print(df.head())
save(df, "./ecolife.xlsx")

sleep(10)
driver.close()
