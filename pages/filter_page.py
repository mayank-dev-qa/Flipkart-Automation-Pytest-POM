from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Filter_Page:

      def __init__(self,driver):
            self.driver=driver
            

      def open_link(self):
            self.driver.get("https://www.flipkart.com")
            time.sleep(3)

      def search_product(self):
            search=self.driver.find_element(By.NAME,"q")
            search.send_keys("iphone 12")
            search.send_keys(Keys.RETURN)
            time.sleep(3)

      def filter(self):
            filters= self.driver.find_element(By.XPATH,"//div[@class='_6i1qKy']")
            filters.click()
            time.sleep(3)

      def filter2(self):
           filter= self.driver.find_element(By.XPATH,"//div[contains(text(),'4★ & above')]")
           filter.click()
           time.sleep(3)

      