import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class HomePage(BasePage):
    
    URL = "https://practicesoftwaretesting.com/"
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.search_input = page.locator("[data-test='search-query']")
        self.product_cards = page.locator("a[data-test^='product-']")
        
    def open(self) -> None:
        self.navigate(self.URL)
        
    def search(self, term: str) -> None:
        self.search_input.fill(term)
        self.search_input.press("Enter")
        
    def verify_products_visible(self) -> None:
        expect(self.product_cards.first).to_be_visible()
        
    def verify_search_results_contain(self, term: str) -> None:
        matching = self.product_cards.filter(has_text=re.compile(term, re.IGNORECASE))
        expect(matching.first).to_be_visible()