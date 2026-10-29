import pytest
import requests

BASE_URL = "https://api-v1.practicesoftwaretesting.com"

def test_products_api_returns_success(product_response):
    assert product_response.status_code == 200

def test_products_api_returns_product_data(product_response):
    products = product_response.json()
    
    assert isinstance(products, list)
    assert len(products) > 0
    
    for product in products:
        assert "id" in product
        assert "name" in product    
        assert "price" in product
        
        assert isinstance(product["id"], int)
        assert isinstance(product["name"], str)
        assert isinstance(product["price"], (int, float))
    

def test_invalid_endpoint_returns_404():
    response = requests.get(f"{BASE_URL}/invalid-endpoint-for-testing", timeout=10)
    
    assert response.status_code == 404
    
    
def test_product_detail_api_returns_product_data(first_product_id,product_detail_response):
    assert product_detail_response.status_code == 200
    
    product = product_detail_response.json()
    
    assert product["id"] == first_product_id
    assert isinstance(product["name"], str)
    assert isinstance(product["price"], (int, float))
    assert "description" in product
    assert "category" in product
    assert "brand" in product
    
def test_nonexistent_product_returns_404():
    response = requests.get(f"{BASE_URL}/products/9999", timeout=10)
    
    assert response.status_code == 404
    
def test_product_detail_contains_valid_nested_data(product_detail_response):
    assert product_detail_response.status_code == 200
    
    product = product_detail_response.json()
    
    assert isinstance(product["category"],dict)
    assert "id" in product["category"]
    assert "name" in product["category"]
    
    assert isinstance(product["brand"], dict)
    assert "id" in product["brand"]
    assert "name" in product["brand"]
    
    assert isinstance(product["product_image"], dict)
    assert "id" in product["product_image"]
    assert "title" in product["product_image"]
    