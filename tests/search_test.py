import  time
from pages.search_page import Search_Page


def test_valid_search(driver):
   srch= Search_Page(driver)
   srch.open_site()
   srch.search()
   assert "Showing" in driver.page_source

def test_invalid_search_with_results(driver):
   srch= Search_Page(driver)
   srch.open_site()
   srch.search0()
   assert "Showing" in driver.page_source


def test_invalid_search(driver):
   srch= Search_Page(driver)
   srch.open_site()
   srch.search2()
   assert "Sorry, no results found!" in driver.page_source

def test_spcl_chr_search(driver):
   srch= Search_Page(driver)
   srch.open_site()
   srch.search3()
   assert "Sorry, no results found!" in driver.page_source