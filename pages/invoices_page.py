import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class InvoicesPage(BasePage):
    
    URL = "https://practicesoftwaretesting.com/account/invoices"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.invoices_number = page.get_by_role("cell", name=re.compile(r"INV-"))
        
    def open(self) -> None:
        self.navigate(self.URL)
        self.page.wait_for_load_state("networkidle")
        
    def count_invoices(self) -> int:
        return self.invoices_number.count()
    
    def verify_invoice_count(self, expected: int) -> None:
        expect(self.invoices_number).to_have_count(expected, timeout=10000)
