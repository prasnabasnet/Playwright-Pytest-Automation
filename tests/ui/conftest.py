import uuid 
import time 
import pytest
from pages.register_page import RegisterPage
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def registered_user(browser):
    context = browser.new_context()
    page = context.new_page()
    
    email = f"test.user+{int(time.time())}@example.com"
    password = f"Aa1!{uuid.uuid4().hex}"
    
    register_page = RegisterPage(page)
    register_page.open()
    register_page.register(
        first_name="Test",
        last_name="User",
        dob="1990-01-01",
        country="US",
        postal_code="12345",
        house_number="1A",
        phone_number="1234567890",
        email=email,
        password=password
    )
    register_page.verify_registration_sucessful()
    
    context.close()
    return {"email": email,"password": password}

@pytest.fixture(scope="session")
def auth_state(browser, registered_user, tmp_path_factory):
    
    #log in once per run and save the session to a file
    context = browser.new_context()
    page = context.new_page()
    
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(registered_user["email"], registered_user["password"])
    login_page.verify_customer_login_sucessful()
    
    state_file = tmp_path_factory.mktemp("auth")/"state.json"
    context.storage_state(path=str(state_file))
    context.close()
    return str(state_file)

@pytest.fixture
def logged_in_page(new_context, auth_state):
    #Each test gets a fresh browser context with the logged-in state loaded
    context = new_context(storage_state=auth_state)
    return context.new_page()