from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/l.jinnmen/Documents/python/chromedriver")

driver.set_page_load_timeout("10")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
driver.find_element_by_name("btnK").click()
time.sleep(4)
driver.quit

print "Test completed successfully"

# https://www.youtube.com/watch?v=FFDDN1C1MEQ