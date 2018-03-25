import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class GoogleASearch(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome("/Users/tomokohakata/Documents/jimmy/Python/Selenium/chromedriver")
		
	def test_search_in_google(self):
		driver = self.driver
		driver.set_page_load_timeout("10")
		driver.get("http://google.com")
		driver.find_element_by_name("q").send_keys("Automation Step by Step")
		driver.find_element_by_name("btnK").click()
		time.sleep(4)
		print "Task complete"
		driver.close()
	
	def tearDown(self):
		self.driver.close()
		
if __name__ == "__main__":
	unittest.main()