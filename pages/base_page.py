from playwright.sync_api import Page, expect

class BasePage:
    
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)
        
    def open_cart(self) -> None:
        self.page.locator("[data-test='nav-cart']").click()
        
    def open_account_menu(self) -> None:
        self.page.locator("[data-test='nav-menu']").click()
        
    def sign_out(self) -> None:
        self.open_account_menu()
        self.page.locator("[data-test='nav-sign-out']").click()