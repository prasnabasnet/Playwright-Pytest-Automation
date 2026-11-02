import pytest

from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.smoke
def test_home_page_shows_products(page):
    home_page = HomePage(page)
    home_page.open()
    
    home_page.verify_products_visible()
    
def test_search_returns_matching_products(page):
    home_page = HomePage(page)
    home_page.open()
    
    home_page.search("pliers")
    
    home_page.verify_search_results_contain("pliers")
    
def test_search_with_no_matches_shows_message(page):
    home_page = HomePage(page)
    home_page.open()
    
    home_page.search("zzzzqxqxqx")
    home_page.verify_no_results()
    
def test_clicking_product_opens_its_detail_page(page):
    home_page = HomePage(page)
    home_page.open()
    
    product_name = home_page.open_first_product()
    
    product_page = ProductPage(page)
    product_page.verify_product_details(product_name)
    
@pytest.mark.parametrize(
    "sort_value, descending",
    [("price,asc", False), ("price,desc", True)]
)
def test_sort_by_price(page, sort_value, descending):
    home_page = HomePage(page)
    home_page.open()
    
    home_page.sort_by(sort_value)
    home_page.wait_for_prices_sorted(descending=descending)