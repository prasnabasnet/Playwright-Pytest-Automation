import re

from playwright.sync_api import Page, expect

from pages.base_page import BasePage

class RegisterPage(BasePage):
    
    URL = "https://practicesoftwaretesting.com/auth/register"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_input = page.get_by_label("First name")
        self.last_name_input = page.get_by_label("Last name")
        self.dob_input = page.get_by_label("Date of Birth *")
        self.country_input = page.get_by_label("Country")
        self.postal_code_input = page.get_by_label("Postal code")
        self.house_number_input = page.get_by_label("House number")
        self.phone_number_input = page.get_by_label("Phone")
        self.email_input = page.get_by_label("Email address")
        self.password_input = page.get_by_label("Password")
        self.submit_button = page.locator("[data-test='register-submit']")
        
        
    def open(self) -> None:
        self.navigate(self.URL)
        
    def register(self, first_name,last_name, dob, country, postal_code,house_number, phone_number, email, password) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.dob_input.fill(dob)
        self.country_input.select_option(country)
        self.postal_code_input.fill(postal_code)
        self.house_number_input.fill(house_number)
        self.phone_number_input.fill(phone_number)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
        
    def verify_registration_sucessful(self) ->None:
        expect(self.page).to_have_url(re.compile(r"/auth/login"))