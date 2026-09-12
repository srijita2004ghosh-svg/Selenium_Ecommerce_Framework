import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.config_reader import ConfigReader


class TestUnittestBrowser(unittest.TestCase):

    def setUp(self):

        # Read configuration
        config = ConfigReader.get_config()

        browser = config["DEFAULT"]["browser"]
        base_url = config["DEFAULT"]["base_url"]
        implicit_wait = int(
            config["DEFAULT"]["implicit_wait"]
        )

        # Start Chrome
        if browser.lower() == "chrome":

            options = Options()
            options.add_argument("--start-maximized")

            self.driver = webdriver.Chrome(
                options=options
            )

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        # Configure implicit wait
        self.driver.implicitly_wait(
            implicit_wait
        )

        # Open application
        self.driver.get(base_url)

    def tearDown(self):

        if hasattr(self, "driver"):
            self.driver.quit()

    def test_open_website_using_unittest(self):

        # Verify website title
        self.assertIn(
            "Your Store",
            self.driver.title
        )


if __name__ == "__main__":
    unittest.main()
