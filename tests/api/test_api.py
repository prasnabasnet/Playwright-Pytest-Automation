import requests

BASE_URL = "https://api-v1.practicesoftwaretesting.com"
    
def test_products_api_returns_success():
    response = requests.get(f"{BASE_URL}/products",timeout=10)
    assert response.status_code == 200
    
def test_products_api_returns_product_data():
    response = requests.get(f"{BASE_URL}/products", timeout=10)
    
    products = response.json()
    
    assert isinstance(products, list)
    assert len(products) > 0
    
    first_product = products[0]
    
    assert "id" in first_product
    assert "name" in first_product
    assert "price" in first_product
    
    assert isinstance(first_product["id"], int)
    assert isinstance(first_product["name"], str)
    assert isinstance(first_product["price"], (int, float))
    
def test_invalid_endpoint_returns_404():
    response = requests.get(f"{BASE_URL}/invalid-endpoint-for-testing", timeout=10)
    
    assert response.status_code == 404