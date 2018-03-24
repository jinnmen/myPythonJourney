from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/l.jinnmen/Documents/python/chromedriver")

driver.set_page_load_timeout("10")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("Automation Step by Step")
driver.find_element_by_name("btnK").click()
time.sleep(4)
driver.close()
#driver.quit()

print "Test completed successfully"

# https://www.youtube.com/watch?v=FFDDN1C1MEQ

# Detailed tests and explanations: https://media.readthedocs.org/pdf/selenium-python/latest/selenium-python.pdf
# Test module __main__ explained: https://stackoverflow.com/questions/419163/what-does-if-name-main-do
# To run as application on mac: http://naelshiab.com/tutorial-how-to-automatically-run-your-scripts-on-your-computer/