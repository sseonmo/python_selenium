from selenium import webdriver

rootPath = '..'
driver = webdriver.Chrome(
	executable_path='{}/webdriver/chromedriver77'.format(rootPath)
)

url = 'https://www.facebook.com/'
driver.get(url)

try:
	driver.find_element_by_id('email').send_keys('mo0562@hanmail.net')
	# driver.find_element_by_id('pass').send_keys('Qkr03130208@')
	driver.find_element_by_xpath('// *[ @ id = "pass"]').send_keys('Qkr03130208@')
except:
	driver.find_element_by_name('email').send_keys('mo0562@hanmail.net')
	# driver.find_element_by_name('pass').send_keys('Qkr03130208@')
	driver.find_element_by_xpath('// *[ @ id = "pass"]').send_keys('Qkr03130208@')

for i in range(1, 10):
	id = 'u_0_{}'.format(i)
	try:
		driver.find_element_by_id(id).click()
	except:
		print('{} is not element'.format(id))


