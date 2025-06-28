from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Search_Page:

   def __init__(self,driver):
    self.driver= driver
    
   def open_site(self):
     self.driver.get("https://www.flipkart.com")
     time.sleep(3)

   def search(self):
     name= self.driver.find_element(By.NAME,'q')
     name.send_keys("shoes")
     name.send_keys(Keys.RETURN)
     time.sleep(3)
   
   def search0(self):
     name= self.driver.find_element(By.NAME,'q')
     name.send_keys("axcc")
     name.send_keys(Keys.RETURN)
     time.sleep(3)



   def search2(self):
     name= self.driver.find_element(By.NAME,'q')
     name.send_keys("axccvyu")
     name.send_keys(Keys.RETURN)
     time.sleep(3)

   def search3(self):
     name= self.driver.find_element(By.NAME,'q')
     name.send_keys("@@@####")
     name.send_keys(Keys.RETURN)
     time.sleep(3)


