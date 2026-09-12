from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class ProductSearchPage:

    # --------------------------------
    # Locators
    # --------------------------------

    SEARCH_BOX = (
        By.NAME,
        "search"
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "button.btn.btn-default.btn-lg"
    )

    SEARCH_RESULTS_HEADING = (
        By.XPATH,
        "//h1[contains(text(), 'Search')]"
    )

    PRODUCT_RESULTS = (
        By.CSS_SELECTOR,
        ".product-layout"
    )

    # --------------------------------
    # Constructor
    # --------------------------------

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )

        self.logger = Logger.get_logger(
            self.__class__.__name__
        )

    # --------------------------------
    # Enter Search Text
    # --------------------------------

    def enter_search_text(self, product_name):

        self.logger.info(
            f"Entering product search text: {product_name}"
        )

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

        search_box.clear()
        search_box.send_keys(product_name)

        self.logger.info(
            "Product search text entered successfully"
        )

    # --------------------------------
    # Click Search Button
    # --------------------------------

    def click_search_button(self):

        self.logger.info(
            "Clicking search button"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        ).click()

        self.logger.info(
            "Search button clicked successfully"
        )

    # --------------------------------
    # Search Product
    # --------------------------------

    def search_product(self, product_name):

        self.logger.info(
            f"Starting product search for: {product_name}"
        )

        self.enter_search_text(
            product_name
        )

        self.click_search_button()

        self.logger.info(
            f"Product search completed for: {product_name}"
        )

    # --------------------------------
    # Get Search Results Heading
    # --------------------------------

    def get_search_results_heading(self):

        self.logger.info(
            "Reading search results heading"
        )

        heading = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_RESULTS_HEADING
            )
        )

        heading_text = heading.text.strip()

        self.logger.info(
            f"Search results heading: {heading_text}"
        )

        return heading_text

    # --------------------------------
    # Check Product Results
    # --------------------------------

    def are_products_displayed(self):

        self.logger.info(
            "Checking whether products are displayed"
        )

        products = self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_RESULTS
            )
        )

        result = len(products) > 0

        self.logger.info(
            f"Products displayed: {result}"
        )

        return result