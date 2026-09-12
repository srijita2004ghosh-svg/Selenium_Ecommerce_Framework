from base.base_test import BaseTest
from pages.product_search_page import ProductSearchPage


class TestProductSearch(BaseTest):

    def test_product_search(self):

        product_search_page = ProductSearchPage(self.driver)

        # Search for a product
        product_search_page.search_product("iPhone")

        # Print search information
        print(
            "Current URL:",
            self.driver.current_url
        )

        print(
            "Page Title:",
            self.driver.title
        )

        print(
            "Search Results Heading:",
            product_search_page.get_search_results_heading()
        )

        # Validate search results
        assert product_search_page.are_products_displayed(), \
            "No products were displayed in search results"