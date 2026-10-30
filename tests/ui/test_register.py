import time
import uuid

from pages.register_page import RegisterPage

def test_register_new_user(page):
    register_page = RegisterPage(page)
    register_page.open()
    
    email = f"test.user+{int(time.time())}@example.com"
    password = f"Aa1!{uuid.uuid4().hex[:8]}"
    
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