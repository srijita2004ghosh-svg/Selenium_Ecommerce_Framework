from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.config_reader import ConfigReader
from utilities.screenshot import ScreenshotUtil
from utilities.logger import Logger


class BaseTest:

    # --------------------------------
    # Setup
    # --------------------------------

    def setup_method(self):
        self.logger = Logger.get_logger(self.__class__.__name__)

        self.logger.info("Starting test setup")

        config = ConfigReader.get_config()

        browser = config["DEFAULT"]["browser"]
        base_url = config["DEFAULT"]["base_url"]
        implicit_wait = int(
            config["DEFAULT"]["implicit_wait"]
        )

        self.logger.info(
            f"Browser selected: {browser}"
        )

        if browser.lower() == "chrome":

            options = Options()
            options.add_argument("--start-maximized")

            self.driver = webdriver.Chrome(
                options=options
            )

            self.logger.info(
                "Chrome WebDriver started successfully"
            )

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        self.driver.implicitly_wait(
            implicit_wait
        )

        self.logger.info(
            f"Implicit wait configured: {implicit_wait} seconds"
        )

        self.driver.get(base_url)

        self.logger.info(
            f"Opened application: {base_url}"
        )

    # --------------------------------
    # Teardown
    # --------------------------------

    def teardown_method(self):

        if hasattr(self, "driver"):

            self.logger.info(
                "Starting test teardown"
            )

            try:

                self.driver.quit()

                self.logger.info(
                    "Browser closed successfully"
                )

            except Exception as error:

                self.logger.error(
                    f"Error while closing browser: {error}"
                )