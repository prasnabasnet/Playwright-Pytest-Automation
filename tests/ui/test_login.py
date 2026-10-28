from pages.login_page import LoginPage

def test_login_page_loads(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.is_login_heading_visible()