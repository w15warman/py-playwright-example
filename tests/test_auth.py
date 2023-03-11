import pytest
import pages
import time


class TestAuth:
    def test_auth_valid_creds(self, page):
        pages.login_page.open_login_page(page)
        pages.login_page.login(page, 'standard_user', 'secret_sauce')
        pages.inventory_page.validate_page_title(page)
        time.sleep(10)
