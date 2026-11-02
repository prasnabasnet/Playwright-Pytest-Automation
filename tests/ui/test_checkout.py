import pytest

from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.smoke
def test_checkout_process(logged_in_page):
    page = logged_in_page
    home_page = HomePage(page)
    home_page.open()
    home_page.open_first_product()
    
    product_page = ProductPage(page)
    product_page.add_to_cart()
    product_page.open_cart()
    
    checkout_page = CheckoutPage(page)
    checkout_page.proceed_from_cart()
    checkout_page.proceed_from_sign_in()
    checkout_page.fill_billing_address(postal_code="12345", house_number="10")
    checkout_page.pay_with_method(method="cash-on-delivery")
    checkout_page.place_order()