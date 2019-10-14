from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(
    executable_path='../webdriver/chromedriver'
)

url = 'https://www.instagram.com/explore/tags/%EC%8A%A4%EC%9C%99%EB%8C%84%EC%8A%A4/?hl=ko'
driver.get(url)     # 동작 후 기본 enter
sleep(5)
pageString = driver.page_source
print(pageString)

# 인스타 껍데이
# 인스타 내용 _9AhH0

driver.close()

