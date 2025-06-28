import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Buynow_Page:

      def __init__(self,driver):
            self.driver= driver

      def open_link(self):
            self.driver.get("https://www.flipkart.com")
            time.sleep(3)

      def search_prod(self):
            input= self.driver.find_element(By.NAME,'q')
            input.send_keys("ps5")
            input.send_keys(Keys.RETURN)
            time.sleep(3)
      
      def sel_product(self):
       product= self.driver.find_element(By.XPATH, "//a[@class='wjcEIp']")
       product.click()
       time.sleep(4)
       self.driver.switch_to.window(self.driver.window_handles[1])


      def buynow(self):
            btn=self.driver.find_element(By.XPATH, "//button[contains(@class,'QqFHMw') and contains(@class,'vslbG+') and contains(@class,'_3Yl67G') and contains(@class,'_7Pd1Fp')]")
            btn.click()
            time.sleep(3)

      def loginflow(self):
           login=self.driver.find_element(By.XPATH, "//input[contains(@class,'r4vIwl') and contains(@class,'Jr-g+f')]")
           login.send_keys("7067614295")
           login.send_keys(Keys.RETURN)
           time.sleep(3)

      

      