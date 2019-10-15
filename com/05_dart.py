from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(
	executable_path='../webdriver/chromedriver'
)

url = 'http://dart.fss.or.kr/'

driver.get(url)

driver.find_element_by_id('textCrpNm').send_keys('셀트리온')
element = driver.find_element_by_tag_name('input')
driver.find_element_by_xpath('//*[@id="searchForm"]/fieldset/p[4]/input').click()
sleep(5)
#  여러 요소일경우 elements 사용
driver.find_elements_by_xpath('//*[@id="checkCorpSelect"]')[1].click()
driver.find_element_by_xpath('//*[@id="corpListContents"]/div/fieldset/div[3]/a[1]/img').click()


# 두번째 검색버튼
driver.find_element_by_xpath('//*[@id="searchpng"]').click()
pageString = driver.page_source
print(pageString)

sleep(10)
driver.close()




