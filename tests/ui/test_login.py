from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_page_loads(page):
    login_page = LoginPage(page)
    login_page.open()
    assert login_page.page.url == login_page.URL
    login_page.verify_login_form_visible()

def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.open()
    
    login_page.login("invalid-user@example.com", "WrongPassword123!")
    login_page.verify_login_failed()
    
def test_login_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.open()
    
    login_page.login("admin@practicesoftwaretesting.com", "welcome01")
    login_page.verify_login_sucessful()
    
def test_login_with_empty_fields(page):
    login_page = LoginPage(page)
    login_page.open()
    
    login_page.login("", "")
    login_page.verify_required_fields_errors()
    expect(login_page.page).to_have_url(login_page.URL)

    