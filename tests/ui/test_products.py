from pages.home_page import HomePage

def test_home_page_shows_products(page):
    home_page = HomePage(page)
    home_page.open()
    
    home_page.verify_products_visible()
    
def test_search_returns_matching_products(page):
    home_page = HomePage(page)
    home_page.open()
    
    home_page.search("pliers")
    
    home_page.verify_search_results_contain("pliers")