from playwright.sync_api import Page
import config


class InventoryPage:
    _PAGE_TITTLE = "//div[@class='app_logo']"

    def validate_page_title(self, page: Page) -> None:
        title = page.locator(self._PAGE_TITTLE).text_content()
        assert title == 'Swag Labs', 'Page title changed'

