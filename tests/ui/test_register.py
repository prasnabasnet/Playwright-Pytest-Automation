import time
import uuid
import re
from playwright.sync_api import expect

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
    register_page.verify_registration_successful()
    
def _unique_email() -> str:
    return f"test.user+{int(time.time() * 1000)}@example.com"


VALID = dict(
    first_name="Test",
    last_name="User",
    dob="1990-01-01",
    country="US",
    postal_code="12345",
    house_number="1A",
    phone_number="1234567890",
)


def test_register_with_empty_fields_shows_required_errors(page):
    register_page = RegisterPage(page)
    register_page.open()

    register_page.submit()

    register_page.verify_still_on_register_page()
    register_page.verify_error("First name is required")
    register_page.verify_error("Last name is required")
    register_page.verify_error("Email is required")
    register_page.verify_error("Password is required")


def test_register_with_existing_email_is_rejected(page, registered_user):
    register_page = RegisterPage(page)
    register_page.open()

    register_page.register(
        **VALID,
        email=registered_user["email"],
        password=f"Aa1!{uuid.uuid4().hex[:8]}",
    )

    register_page.verify_still_on_register_page()
    register_page.verify_error(re.compile(r"already exists", re.I))


def test_register_with_invalid_email_is_rejected(page):
    register_page = RegisterPage(page)
    register_page.open()

    register_page.register(
        **VALID,
        email="not-an-email",
        password=f"Aa1!{uuid.uuid4().hex[:8]}",
    )

    register_page.verify_still_on_register_page()
    register_page.verify_error(re.compile(r"email", re.I))


def test_register_with_weak_password_is_rejected(page):
    register_page = RegisterPage(page)
    register_page.open()

    register_page.register(**VALID, email=_unique_email(), password="abc")

    register_page.verify_still_on_register_page()
    register_page.verify_error(re.compile(r"password", re.I))
    