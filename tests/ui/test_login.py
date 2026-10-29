from pages.login_page import LoginPage

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