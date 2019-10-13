from selenium import webdriver

driver = webdriver.Chrome(
    executable_path='../webdriver/chromedriver'
)

url = 'https://www.instagram.com/explore/tags/%EC%8A%A4%EC%9C%99%EB%8C%84%EC%8A%A4/?hl=ko'
driver.get(url)

# driver.close()
