import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class HomePage(BasePage):
    
    URL = "https://practicesoftwaretesting.com/"
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.search_input = page.locator("[data-test='search-query']")
        self.product_cards = page.locator("a[data-test^='product-']")
        self.no_results_message = page.get_by_text("There are no products found")
        self.results_summary = page.get_by_text("0 products found for")
        
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
        
    def verify_no_results(self) -> None:
        expect(self.results_summary).to_be_visible()
        expect(self.no_results_message).to_be_visible()
        
    def open_first_product(self) -> str:
        card = self.product_cards.first
        name = card.locator("[data-test='product-name']").inner_text().strip()
        card.click()
        return name
        