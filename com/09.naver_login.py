from libs.chromedriver77 import getDriver
from time import sleep

driver = getDriver()
url = 'https://www.naver.com'

driver.get(url)

driver.find_element_by_xpath('//*[@id="account"]/div/a').click()
driver.find_element_by_xpath('//*[@id="id"]').send_keys('mo0562')
driver.find_element_by_xpath('//*[@id="pw"]').send_keys('Pkr03130208@')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# driver.execute_script() 스크립트 실행

sleep(25)
# 수동로그인
# 중고나라
url = 'https://cafe.naver.com/joonggonara'
driver.get(url)

keyword = '감기'
driver.find_element_by_xpath('//*[@id="topLayerQueryInput"]').send_keys(keyword)
driver.find_element_by_xpath('//*[@id="cafe-search"]/form/button').click()
driver.switch_to_frame('cafe_main')
sleep(3)
pageString = driver.page_source
file = open("./joonggonara.html", "w+")
file.write(pageString)

# sleep(30)
# driver.close()


