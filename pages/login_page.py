from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://practicesoftwaretesting.com/auth/login/"

    def __init__(self, page: Page):
        super().__init__(page)

        self.login_heading = page.get_by_role("heading", name="Login")


    def open(self) -> None:
        self.navigate(self.URL)

    def is_login_heading_visible(self) -> None:
        expect(self.login_heading).to_be_visible()
