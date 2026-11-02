import re
from playwright .sync_api import Page, expect
from pages.base_page import BasePage

class CartPage(BasePage):
    
    def __init__(self,page: Page):
        super().__init__(page)
        
        self.product_title = page.locator("[data-test='product-title']")
        self.product_quantity = page.locator("[data-test='product-quantity']")
        self.line_price = page.locator("[data-test='line-price']")
        
    def verify_item_in_cart(self, expected_name: str, expected_quantity: str = "1") ->None:
        expect(self.page).to_have_url(re.compile(r"/checkout"))
        expect(self.product_title).to_contain_text(expected_name)
        expect(self.product_quantity).to_have_value(expected_quantity)
        expect(self.line_price).to_be_visible()