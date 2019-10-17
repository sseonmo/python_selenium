from libs.crawler import crawl
from bs4 import BeautifulSoup

url = 'http://dart.fss.or.kr/corp/searchAutoComplete.do?textCrpNm={}_=1571346383827'.format('삼성')
pageString = crawl(url)
# print(pageString)
bsObj = BeautifulSoup(pageString, 'html.parser')
print(bsObj)
