import pytest

from pages.buynowflow_page import Buynow_Page

# Buy now without login

def test_buy_without_login(driver):
    buy= Buynow_Page(driver)
    buy.open_link()
    buy.search_prod()
    buy.sel_product()
    buy.buynow()
    assert "Login or Signup" in driver.page_source

# buy now flow with login opt sent

def test_buy_with_login_opt_sent(driver):
    buy= Buynow_Page(driver)
    buy.open_link()
    buy.search_prod()
    buy.sel_product()
    buy.buynow()
    buy.loginflow()
    assert "Enter OTP" in driver.page_source

