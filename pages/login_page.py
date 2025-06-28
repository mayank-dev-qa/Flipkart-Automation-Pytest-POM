from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_site(self):
        self.driver.get("https://www.flipkart.com")
        time.sleep(3)

    def click_login(self):
        login_btn = self.driver.find_element(By.XPATH, "//span[text()='Login']")
        login_btn.click()
        time.sleep(2)

    def input_no(self, number):
        input_box = self.driver.find_element(By.XPATH, "//input[contains(@class,'r4vIwl')and contains(@class,'BV+Dqf')]")
        input_box.send_keys(number)
        time.sleep(2)

    def otp_req(self):
        req_btn = self.driver.find_element(By.XPATH, "//button[contains(@class,'QqFHMw') and contains(@class,'twnTnD') and contains(@class,'_7Pd1Fp')]")
        req_btn.click()
        time.sleep(2)