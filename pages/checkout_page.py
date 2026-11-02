import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    
    def __init__(self,page: Page):
        super().__init__(page)
        
        self.proceed_from_cart_button = page.locator("[data-test='proceed-1']")
        self.proceed_from_sign_in_button = page.locator("[data-test='proceed-2']")
        self.postal_code_input = page.locator("[data-test='postal_code']")
        self.house_number_input = page.locator("[data-test='house_number']")
        self.proceed_to_payment_button = page.locator("[data-test='proceed-3']")
        self.payment_method_select = page.locator("[data-test='payment-method']")
        self.finish_button = page.locator("[data-test='finish']")
        
    def proceed_from_cart(self) -> None:
        expect(self.proceed_from_cart_button).to_be_enabled(timeout=10000)
        self.proceed_from_cart_button.click()
        
    def proceed_from_sign_in(self) -> None:
        expect(self.proceed_from_sign_in_button).to_be_enabled(timeout=10000)
        self.proceed_from_sign_in_button.click()
        
    def fill_billing_address(self, postal_code: str, house_number: str) -> None:
        self.postal_code_input.fill(postal_code)
        self.house_number_input.fill(house_number)
        expect(self.proceed_to_payment_button).to_be_enabled(timeout=10000)
        self.proceed_to_payment_button.click()
        
    def pay_with_method(self,method: str) -> None:
        self.payment_method_select.select_option(method)
        self.finish_button.click()
        expect(self.page.get_by_text("Payment was successful")).to_be_visible()
        
    def place_order(self) -> None:
        self.finish_button.click()
        expect(self.page.get_by_text(re.compile(r'Thanks for your order'))).to_be_visible()