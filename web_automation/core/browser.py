
"""
Shared visible Google Chrome lifecycle for JE BikeZ automation.
"""

from contextlib import contextmanager
from typing import Iterator

from playwright.sync_api import Browser, Page, sync_playwright

from web_automation.config.config import TIMEOUT


@contextmanager
def browser_page(headless: bool = False) -> Iterator[Page]:
    """
    Launch visible Google Chrome and provide a reusable page.

    Chrome closes automatically when the test suite finishes.
    """

    with sync_playwright() as playwright:
        browser_type = playwright.chromium

        browser: Browser = browser_type.launch(
            channel="chrome",
            headless=headless,
        )

        try:
            page: Page = browser.new_page()
            page.set_default_timeout(TIMEOUT)
            page.set_default_navigation_timeout(TIMEOUT)

            yield page

        finally:
            browser.close()
