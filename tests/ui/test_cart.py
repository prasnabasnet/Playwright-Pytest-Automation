from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_add_product_to_cart(page):
    home_page = HomePage(page)
    home_page.open()
    product_name = home_page.open_first_product()
    
    product_page = ProductPage(page)
    product_page.add_to_cart()
    product_page.open_cart()
    
    cart_page = CartPage(page)
    cart_page.verify_item_in_cart(product_name)