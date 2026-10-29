import pytest
from clients.api_client import ApiClient

@pytest.fixture(scope="session")
def api_client():
    return ApiClient()


@pytest.fixture
def product_response(api_client):
    return api_client.get_products()

@pytest.fixture
def first_product_id(product_response):
    products = product_response.json()[0]["id"]
    if products:
        return products
    
@pytest.fixture
def product_detail_response(api_client, first_product_id):
    return api_client.get_product(first_product_id)