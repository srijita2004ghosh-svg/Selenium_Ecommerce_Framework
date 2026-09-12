from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class LoginPage:

    # --------------------------------
    # Locators
    # --------------------------------

    MY_ACCOUNT = (
        By.XPATH,
        "//span[text()='My Account']"
    )

    LOGIN_LINK = (
        By.LINK_TEXT,
        "Login"
    )

    EMAIL_FIELD = (
        By.ID,
        "input-email"
    )

    PASSWORD_FIELD = (
        By.ID,
        "input-password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//input[@value='Login']"
    )

    ACCOUNT_HEADING = (
        By.XPATH,
        "//h2[contains(text(), 'My Account')]"
    )

    LOGIN_ERROR = (
        By.CSS_SELECTOR,
        ".alert-danger"
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
    # Click My Account
    # --------------------------------

    def click_my_account(self):

        self.logger.info(
            "Clicking My Account"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.MY_ACCOUNT
            )
        ).click()

        self.logger.info(
            "My Account clicked successfully"
        )

    # --------------------------------
    # Click Login
    # --------------------------------

    def click_login(self):

        self.logger.info(
            "Clicking Login link"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_LINK
            )
        ).click()

        self.logger.info(
            "Login link clicked successfully"
        )

    # --------------------------------
    # Enter Email
    # --------------------------------

    def enter_email(self, email):

        self.logger.info(
            "Entering email address"
        )

        email_field = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL_FIELD
            )
        )

        email_field.clear()
        email_field.send_keys(email)

        self.logger.info(
            "Email address entered successfully"
        )

    # --------------------------------
    # Enter Password
    # --------------------------------

    def enter_password(self, password):

        self.logger.info(
            "Entering password"
        )

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD_FIELD
            )
        )

        password_field.clear()
        password_field.send_keys(password)

        self.logger.info(
            "Password entered successfully"
        )

    # --------------------------------
    # Click Login Button
    # --------------------------------

    def click_login_button(self):

        self.logger.info(
            "Clicking Login button"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        ).click()

        self.logger.info(
            "Login button clicked successfully"
        )

    # --------------------------------
    # Check Login Error
    # --------------------------------

    def get_login_error(self):

        try:

            error = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.visibility_of_element_located(
                    self.LOGIN_ERROR
                )
            )

            error_message = error.text.strip()

            self.logger.warning(
                f"Login error displayed: {error_message}"
            )

            return error_message

        except Exception:

            return None

    # --------------------------------
    # Check Successful Login
    # --------------------------------

    def is_login_successful(self):

        self.logger.info(
            "Validating login result"
        )

        WebDriverWait(
            self.driver,
            10
        ).until(
            lambda driver: (
                "account/account" in driver.current_url
                or "account/login" in driver.current_url
            )
        )

        error_message = self.get_login_error()

        if error_message:

            self.logger.error(
                "Login failed because of invalid credentials"
            )

            raise AssertionError(
                f"Login failed. Website message: "
                f"{error_message}"
            )

        try:

            result = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.ACCOUNT_HEADING
                )
            ).is_displayed()

            self.logger.info(
                "Login successful - My Account page displayed"
            )

            return result

        except Exception:

            self.logger.error(
                "Login validation failed"
            )

            raise AssertionError(
                "Login did not succeed. "
                f"Current URL: {self.driver.current_url}"
            )

    # --------------------------------
    # Complete Login
    # --------------------------------

    def login(self, email, password):

        self.logger.info(
            "Starting login process"
        )

        self.click_my_account()
        self.click_login()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

        self.logger.info(
            "Login process completed"
        )