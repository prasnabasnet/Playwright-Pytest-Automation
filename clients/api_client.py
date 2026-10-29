import requests

BASE_URL = "https://api-v1.practicesoftwaretesting.com"

class ApiClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        
    def get(self,path):
        return self.session.get(f"{self.base_url}{path}", timeout=10)
    
    def get_products(self):
        return self.get("/products")
    
    def get_product(self, product_id):
        return self.get(f"/products/{product_id}")