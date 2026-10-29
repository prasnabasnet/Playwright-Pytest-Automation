import requests
import pytest

BASE_URL = "https://api-v1.practicesoftwaretesting.com"

@pytest.fixture
def product_response():
    response = requests.get(f"{BASE_URL}/products",timeout=10)
    return response

@pytest.fixture
def first_product_id(product_response):
    products = product_response.json()[0]["id"]
    if products:
        return products
    
@pytest.fixture
def product_detail_response(first_product_id):
    response = requests.get(f"{BASE_URL}/products/{first_product_id}",timeout=10)
    return response