import pytest
from pages.filter_page import Filter_Page

 
 # applying a single filter

def test_applying_filter(driver):
    fltr=Filter_Page(driver)
    fltr.open_link()
    fltr.search_product()
    fltr.filter()
    assert 'Clear all' in driver.page_source


# Applying 2 filters at a time

def test_applying_two_filter(driver):
    fltr=Filter_Page(driver)
    fltr.open_link()
    fltr.search_product()
    fltr.filter()
    fltr.filter2()
    assert 'Clear all' in driver.page_source
