import pytest
import time
from pages.login_page import LoginPage


def test_valid_login(driver):
    login = LoginPage(driver)
    login.open_site()
    login.click_login()
    login.input_no("9303909875")
    login.otp_req()
    assert "Please enter the OTP sent to" in driver.page_source

def test_invalid_login_no(driver):
    login= LoginPage(driver)
    login.open_site()
    login.click_login()
    login.input_no("776654434334")
    login.otp_req()
    assert "Please enter valid Email ID/Mobile number" in driver.page_source

def test_blank_invalid_login(driver):
    login= LoginPage(driver)
    login.open_site()
    login.click_login()
    login.input_no("")
    login.otp_req()
    assert "Please enter valid Email ID/Mobile number" in driver.page_source

     