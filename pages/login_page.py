from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://practicesoftwaretesting.com/auth/login/"

    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.login_heading = page.get_by_role("heading", name="Login")


    def open(self) -> None:
        self.navigate(self.URL)

    def login(self,email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_heading_visible(self) -> None:
        expect(self.login_heading).to_be_visible()
