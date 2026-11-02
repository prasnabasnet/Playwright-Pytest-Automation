import re
from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class ProductPage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.name = page.locator("[data-test='product-name']")
        self.unit_price = page.locator("[data-test='unit-price']")
        self.add_to_cart_button = page.locator("[data-test='add-to-cart']")
        
    def verify_product_details(self, expected_name: str) -> None:
        expect(self.page).to_have_url(re.compile(r"/product/"))
        expect(self.name).to_have_text(expected_name)
        expect(self.unit_price).to_be_visible()
        expect(self.add_to_cart_button).to_be_visible()