from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("http://github.com/ShiinaOrez")

shiina_id=driver.find_element_by_id()

print (shiina_id)

driver.close()
