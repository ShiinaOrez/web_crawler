from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get("http://www.python.org")
assert "Pyhton" in driver.title
elem=driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
