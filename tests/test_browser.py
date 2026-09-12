from base.base_test import BaseTest


class TestBrowser(BaseTest):

    def test_open_website(self):
        assert "Your Store" in self.driver.title