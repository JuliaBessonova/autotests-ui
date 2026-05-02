from re import Pattern
from tools.logger import get_logger
from playwright.sync_api import Page, expect

logger = get_logger("BASE_COMPONENT")

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]) -> None:
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        logger.info(step)
        expect(self.page).to_have_url(expected_url)

    def refresh_page(self):
        self.page.reload()