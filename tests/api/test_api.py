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
    
def test_product_detail_api_returns_product_data():
    
    response =requests.get(f"{BASE_URL}/products/1", timeout=10)
    
    assert response.status_code == 200
    
    product = response.json()
    
    assert isinstance(product, dict)
    assert product["id"] == 1
    assert product["name"] == "Combination Pliers"
    assert isinstance(product["price"], (int, float))
    assert "description" in product
    assert "category" in product
    assert "brand" in product
    
def test_nonexistent_product_returns_404():
    response = requests.get(f"{BASE_URL}/products/9999", timeout=10)
    
    assert response.status_code == 404