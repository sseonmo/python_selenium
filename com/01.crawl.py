import requests
from libs.crawler import  crawl

url = 'https://www.instagram.com/explore/tags/%ED%8E%A0%EB%A6%AC%EC%84%B8%EC%9D%B4%EB%93%9C/?hl=ko'
pageString = crawl(url)
print(pageString)
