from base.base_test import BaseTest
from pages.login_page import LoginPage
from utilities.csv_reader import CSVReader


class TestLogin(BaseTest):

    def test_valid_login(self):

        test_data = CSVReader.read_login_data()

        email = test_data[0]["email"]
        password = test_data[0]["password"]

        login_page = LoginPage(self.driver)

        login_page.login(email, password)

        print("Current URL:", self.driver.current_url)
        print("Page Title:", self.driver.title)

        assert login_page.is_login_successful(), \
            "Login was not successful"