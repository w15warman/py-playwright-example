from playwright.sync_api import Page
import config


class LoginPage:

    def open_login_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)
