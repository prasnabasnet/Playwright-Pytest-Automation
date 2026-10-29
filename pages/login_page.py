import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://practicesoftwaretesting.com/auth/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("input[type='submit']")
        self.login_heading = page.locator("h3:has-text('Login')")

    def open(self) -> None:
        self.navigate(self.URL)

    def verify_login_form_visible(self) -> None:
        expect(self.login_heading).to_be_visible()
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_visible()
        
    def login(self,email: str,password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        
    def verify_login_failed(self) -> None:
        expect(self.page.get_by_text("Invalid email or password")).to_be_visible()
        
    def verify_login_sucessful(self)-> None:
        expect(self.page).to_have_url(re.compile(r"/admin/dashboard"))
        
    def verify_required_fields_errors(self) -> None:
        expect(self.page.get_by_text("Email is required")).to_be_visible()
        expect(self.page.get_by_text("Password is required")).to_be_visible()