import allure
import pytest
import pages


@allure.feature("Auth")
class TestAuth:

    @allure.title("Login with valid creds")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_auth_valid_creds(self, page):
        pages.login_page.open_login_page(page)
        pages.login_page.login(page, "standard_user", "secret_sauce")
        pages.inventory_page.validate_page_title(page)

    @allure.title("Login with invalid creds")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_invalid_creds(self, page):
        pages.login_page.open_login_page(page)
        pages.login_page.login(page, "standard_user", "invalid_password")
        pages.login_page.validate_error_message(page, "Epic sadface: Username and password do not match any user in this service1")

    @allure.title("Locked user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_locked_user(self, page):
        pages.login_page.open_login_page(page)
        pages.login_page.login(page, "locked_out_user", "secret_sauce")
        pages.login_page.validate_error_message(page, "Epic sadface: Sorry, this user has been locked out.")
