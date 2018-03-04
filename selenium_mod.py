from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver=webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')

driver.get("http://github.com/ShiinaOrez")

driver.driver.get_screenshot_as_file("shiina.png")

with open("shiina.html","w") as f:
	
	f.write(driver.page_source)

driver.close()
