import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import time
from decimal import Decimal

class HomePage(BasePage):
    
    URL = "https://practicesoftwaretesting.com/"
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.search_input = page.locator("[data-test='search-query']")
        self.product_cards = page.locator("a[data-test^='product-']")
        self.no_results_message = page.get_by_text("There are no products found")
        self.results_summary = page.get_by_text("0 products found for")
        self.sort_select =page.locator("[data-test='sort']")
        
    def open(self) -> None:
        self.navigate(self.URL)
        
    def search(self, term: str) -> None:
        expect(self.product_cards.first).to_be_visible()
        self.search_input.fill(term)
        self.search_input.press("Enter")
        
    def verify_products_visible(self) -> None:
        expect(self.product_cards.first).to_be_visible()
        
    def verify_search_results_contain(self, term: str) -> None:
        matching = self.product_cards.filter(has_text=re.compile(term, re.IGNORECASE))
        expect(matching.first).to_be_visible()
        
    def verify_no_results(self) -> None:
        expect(self.results_summary).to_be_visible(timeout=10000)
        expect(self.no_results_message).to_be_visible()
        
    def open_first_product(self) -> str:
        card = self.product_cards.filter(has_not_text="Out of stock").first
        name = card.locator("[data-test='product-name']").inner_text().strip()
        card.click()
        return name
    
    def sort_by(self, value: str) -> None:
        expect(self.product_cards.first).to_be_visible()
        self.sort_select.select_option(value)
        
    def get_card_prices(self) -> list[Decimal]:
        # Read the "$ 14.15" style prices out fo the text of every product card and convert them to Decimal values
        prices =[]
        for text in self.product_cards.all_inner_texts():
            match = re.search(r"\$(\d+\.\d{2})", text)
            if match:
                prices.append(Decimal(match.group(1)))
        return prices
    
    def wait_for_prices_sorted(self, descending: bool = False, timeout: float = 10.0)    -> list[Decimal]:
        
        deadline = time.monotonic() + timeout
        while True:
            prices = self.get_card_prices()
            if len(prices) > 1 and prices == sorted(prices, reverse=descending):
                return prices
            if time.monotonic() > deadline:
                direction = "descending" if descending else "ascending"
                raise AssertionError(f"Prices were not sorted in {direction} order within {timeout} seconds: {prices}")
            self.page.wait_for_timeout(500)  
            
    def filter_by_category(self,name:str) -> None:
        expect(self.product_cards.first).to_be_visible()
        self.page.get_by_role("checkbox", name=name, exact=True).check()
        
    def wait_for_all_products_to_contain(self, term: str, timeout: float = 10.0) -> list[str]:
        #After ticking a filter, keep checking until every card name contains the term 
        deadline = time.monotonic() + timeout
        while True:
            names = self.product_cards.locator("[data-test='product-name']").all_inner_texts()
            if names and all(term.lower() in n.lower() for n in names):
                return names
            if time.monotonic() > deadline:
                raise AssertionError(f"Not every product contains '{term}': {names}")
            self.page.wait_for_timeout(300)
            