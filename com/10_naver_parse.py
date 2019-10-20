from bs4 import BeautifulSoup


def parse(pageString):
	bsObj = BeautifulSoup(pageString, 'html.parser')
	articleBoard = bsObj.findAll('div', {'class': 'article-board result-board m-tcol-c'})
	print(articleBoard[0])
	return []

file = open('joonggonara.html')
pageString = file.read()
list = parse(pageString)