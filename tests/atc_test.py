import pytest
import time
from pages.atc_page import ATC_page

def test_add_to_cart(driver):
      atc= ATC_page(driver)
      atc.open_site()
      atc.enter_product_name()
      atc.select_product()
      atc.atc_btn()
      assert "Place Order" in driver.page_source

def test_variant_sel(driver):
      atc= ATC_page(driver)
      atc.open_site()
      atc.enter_product_name()
      atc.select_product()
      atc.select_product_var()
      atc.atc_btn()
      assert "Place Order" in driver.page_source

def test_out_of_stock_atc(driver):
      atc= ATC_page(driver)
      atc.open_site()
      atc.enter_product_name2()
      atc.select_product2()
      assert 'Sold Out'  in driver.page_source

def test_atc_then_remove(driver):
      atc= ATC_page(driver)
      atc.open_site()
      atc.enter_product_name()
      atc.select_product()
      atc.atc_btn()
      atc.product_remove()
      atc.remove_btnn()
      assert "Missing Cart items?" in driver.page_source




