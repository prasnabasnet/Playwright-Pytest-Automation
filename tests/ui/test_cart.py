import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.smoke
def test_add_product_to_cart(page):
    home_page = HomePage(page)
    home_page.open()
    product_name = home_page.open_first_product()
    
    product_page = ProductPage(page)
    product_page.add_to_cart()
    product_page.open_cart()
    
    cart_page = CartPage(page)
    cart_page.verify_item_in_cart(product_name)
    
def test_changing_quantity_updates_line_price_and_total(page):
    home_page= HomePage(page)
    home_page.open()
    home_page.open_first_product()
    
    product_page = ProductPage(page)
    product_page.add_to_cart()
    product_page.open_cart()
    
    cart_page = CartPage(page)
    unit_price = cart_page.get_unit_price()
    cart_page.set_quantity("3")
    
    cart_page.verify_line_price_and_total(unit_price * 3)