from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.invoices_page import InvoicesPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from playwright.sync_api import Page, expect

def test_placed_order_appears_in_invoices(logged_in_page):
    page = logged_in_page
    
    invoices_page = InvoicesPage(page)
    invoices_page.open()
    invoices_before = invoices_page.count_invoices()
    
    home_page = HomePage(page)
    home_page.open()
    home_page.open_first_product()
    
    product_page = ProductPage(page)
    product_page.add_to_cart()
    product_page.open_cart()
    
    checkout_page = CheckoutPage(page)
    checkout_page.proceed_from_cart()
    checkout_page.proceed_from_sign_in()
    checkout_page.fill_billing_address(house_number="10")
    checkout_page.pay_with_method(method="cash-on-delivery")
    checkout_page.place_order()
    
    invoices_page.open()
    invoices_page.verify_invoice_count(invoices_before+1)
    
def test_sign_out(page, registered_user):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(registered_user["email"], registered_user["password"])
    login_page.verify_customer_login_sucessful()
    
    login_page.sign_out()
    
    expect(page.locator("[data-test='nav-sign-in']")).to_be_visible()