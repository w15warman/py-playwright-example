from playwright.sync_api import Page
import config


class LoginPage:
    _USERNAME_FIELD = "//input[@id='user-name']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _LOGIN_BUTTON = "//input[@id='login-button']"


    def open_login_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def set_username(self, page: Page, username: str):
        return page.locator(self._USERNAME_FIELD).fill(username)

    def set_password(self, page: Page, password: str):
        return page.locator(self._PASSWORD_FIELD).fill(password)

    def click_login_button(self, page: Page):
        return page.locator(self._LOGIN_BUTTON).click()

    def login(self, page: Page, username: str, password: str) -> None:
        page.locator(self._USERNAME_FIELD).fill(username)
        page.locator(self._PASSWORD_FIELD).fill(password)
        page.locator(self._LOGIN_BUTTON).click()
