import pytest
import pages
import time


class TestAuth:
    def test_auth_valid_creds(self, page):
        pages.login_page.open_login_page(page)
        time.sleep(10)
