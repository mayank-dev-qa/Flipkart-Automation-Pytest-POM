import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ATC_page:
      def __init__(self,driver):
            self.driver= driver
      def open_site(self):
            self.driver.get("https://www.flipkart.com")
            time.sleep(3)

      def enter_product_name2(self):
            name= self.driver.find_element(By.NAME,'q')
            name.send_keys("iphone 12")
            name.send_keys(Keys.RETURN)
            time.sleep(3)

      def enter_product_name(self):
            name= self.driver.find_element(By.NAME,'q')
            name.send_keys("Moto G85")
            name.send_keys(Keys.RETURN)
            time.sleep(3)



     
      def select_product2(self):
            product=self.driver.find_element(By.XPATH,"//div[text()='Apple iPhone 12 (White, 256 GB)']")
            product.click()
            time.sleep(6)

            self.driver.switch_to.window(self.driver.window_handles[1])



      def select_product(self):
            product=self.driver.find_element(By.XPATH,"//div[text()='Motorola G85 5G (Olive Green, 128 GB)']")
            product.click()
            time.sleep(6)

            self.driver.switch_to.window(self.driver.window_handles[1])

      def select_product_var(self):
            var= self.driver.find_element(By.XPATH,"//a[contains(@class,'CDDksN') and contains(@class,'i7n7ZQ')]")
            var.click()
            time.sleep(4)


      def product_remove(self):
       remove = self.driver.find_element(By.XPATH, "//div[text()='Remove']")
       remove.click()
       time.sleep(3)

      def atc_btn(self):
            atc_btn= self.driver.find_element(By.XPATH,"//button[contains(@class, 'QqFHMw') and contains(@class, 'vslbG+') and contains(@class, 'In9uk2')]")
            atc_btn.click()
            time.sleep(3)

      def remove_btnn(self):
            btn= self.driver.find_element(By.XPATH,"//div[text()='Remove']")
            btn.click()
            time.sleep(3)

      

      

      