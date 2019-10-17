from libs.crawler import crawl
from libs.patternMatcher import findMatchedText
from bs4 import BeautifulSoup

url = 'http://dart.fss.or.kr/corp/searchAutoComplete.do?textCrpNm=%EC%85%80%ED%8A%B8%EB%A6%AC%EC%98%A8&_=1571347167311'
pageString = crawl(url)
bsObj = BeautifulSoup(pageString, 'html.parser')
# print(bsObj)

# 테스트, 정규식 -> []
names = findMatchedText(bsObj.text, '셀트리온[가-힣\d\w]*')
print(names)
