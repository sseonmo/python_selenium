from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getDriver():
	rootPath = ".."
	chrome_option = Options()
	driver = webdriver.Chrome(
		executable_path='{}/webDriver/chromedriver77'.format(rootPath),
		options=chrome_option
	)
	return driver
