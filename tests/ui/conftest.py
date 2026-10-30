import uuid 
import time 
import pytest
from pages.register_page import RegisterPage

@pytest.fixture(scope="session")
def registered_user(browser):
    context = browser.new_context()
    page = context.new_page()
    
    email = f"test.user+{int(time.time())}@example.com"
    password = f"Aa1!{uuid.uuid4().hex}"
    
    register_page = RegisterPage()
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