import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture

def driver():
      service_obj= Service(r"C:\Users\HP\Documents\Software Testing\Automation tools\chromedriver-win64\chromedriver.exe")
      driver=webdriver.Chrome(service=service_obj)
      driver.maximize_window()
      yield driver
      driver.quit()