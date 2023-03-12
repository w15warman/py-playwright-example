import allure
from playwright.sync_api import Page
import config


class LoginPage:
    _USERNAME_FIELD = "//input[@id='user-name']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _LOGIN_BUTTON = "//input[@id='login-button']"
    _ERROR_MESSAGE = "//div[@class='error-message-container error']/h3"

    @allure.step("Open the login page")
    def open_login_page(self, page: Page) -> None:
        page.goto(config.host.HOST_URL)

    @allure.step("Login")
    def login(self, page: Page, username: str, password: str) -> None:
        page.locator(self._USERNAME_FIELD).fill(username)
        page.locator(self._PASSWORD_FIELD).fill(password)
        page.locator(self._LOGIN_BUTTON).click()

    @allure.step("Validate error message: {expected_message}")
    def validate_error_message(self, page: Page, expected_message: str):
        actual_message = page.locator(self._ERROR_MESSAGE).text_content()
        assert actual_message == expected_message, "Error message doesn't match"
