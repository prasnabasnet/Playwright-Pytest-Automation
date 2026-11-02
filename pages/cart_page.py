import re
from playwright .sync_api import Page, expect
from pages.base_page import BasePage

from decimal import Decimal

class CartPage(BasePage):
    
    def __init__(self,page: Page):
        super().__init__(page)
        
        self.product_title = page.locator("[data-test='product-title']")
        self.product_quantity = page.locator("[data-test='product-quantity']")
        self.line_price = page.locator("[data-test='line-price']")
        self.unit_price = page.locator("[data-test='product-price']")
        self.cart_total = page.locator("[data-test='cart-total']")
        
    def verify_item_in_cart(self, expected_name: str, expected_quantity: str = "1") ->None:
        expect(self.page).to_have_url(re.compile(r"/checkout"))
        expect(self.product_title).to_contain_text(expected_name)
        expect(self.product_quantity).to_have_value(expected_quantity)
        expect(self.line_price).to_be_visible()
        
    def get_unit_price(self) -> Decimal:
        expect(self.unit_price).to_have_text(re.compile(r"\d"))
        text = self.unit_price.inner_text()
        return Decimal(re.sub(r"[^\d.]", "", text))
        
    def set_quantity(self, quantity: str) ->None:
        self.product_quantity.fill(quantity)
        self.product_quantity.press("Enter")
        
    def verify_line_price_and_total(self, expected: Decimal) -> None:
        expect(self.line_price).to_contain_text(f"{expected:.2f}")
        expect(self.cart_total).to_contain_text(f"{expected:.2f}")
        
        