from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

##executable_path='/Users/rene-ias/Selenium/drivers/geckodriver'
driver = webdriver.Chrome('/Users/rene-ias/Selenium/drivers/chromedriver')
driver.get("http://www.google.com")

elem = driver.find_element_by_name("q")
elem.send_keys("weather")
elem.submit()
elem.send_keys(Keys.ESCAPE)
time.sleep(5)
elem2 = driver.find_element_by_xpath("//span[@id='wob_tm']")
print elem2

time.sleep(5)

print(driver.find_element_by_xpath("//span[@id='wob_tm']"))

driver.quit()
