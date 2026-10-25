
# """
# Shared visible Google Chrome lifecycle for JE BikeZ automation.
# """

# from contextlib import contextmanager
# from typing import Iterator

# from playwright.sync_api import Browser, Page, sync_playwright

# from web_automation.config.config import TIMEOUT


# @contextmanager
# def browser_page(headless: bool = False) -> Iterator[Page]:
#     """
#     Launch visible Google Chrome and provide a reusable page.

#     Chrome closes automatically when the test suite finishes.
#     """

#     with sync_playwright() as playwright:
#         browser_type = playwright.chromium

#         browser: Browser = browser_type.launch(
#             channel="chrome",
#             headless=headless,
#         )

#         try:
#             page: Page = browser.new_page()
#             page.set_default_timeout(TIMEOUT)
#             page.set_default_navigation_timeout(TIMEOUT)

#             yield page

#         finally:
#             browser.close()




"""
Browser management for JE BikeZ Playwright automation.

Local execution:
    Opens a visible browser by default.

GitHub Actions:
    Uses headless mode when CI=true.

Usage:
    with browser_page() as page:
        page.goto("https://je-bikez-frontend.onrender.com")
"""

import os
from contextlib import contextmanager
from typing import Generator

from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)


def is_ci_environment() -> bool:
    """
    Detect whether the test is running in CI.

    GitHub Actions automatically provides CI=true.
    """
    return os.getenv("CI", "").strip().lower() == "true"


@contextmanager
def browser_page() -> Generator[Page, None, None]:
    """
    Launch Playwright, create a browser context and page,
    yield the page to the test, then clean up resources.

    Headed locally; headless in GitHub Actions.
    """
    playwright: Playwright | None = None
    browser: Browser | None = None
    context: BrowserContext | None = None

    try:
        playwright = sync_playwright().start()

        # Use Chromium for consistent local and CI execution.
        browser_type = playwright.chromium

        # Windows: visible browser.
        # GitHub Actions: headless browser.
        headless = is_ci_environment()

        browser = browser_type.launch(
            headless=headless,
            args=["--no-sandbox"] if headless else [],
        )

        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            ignore_https_errors=False,
        )

        page = context.new_page()

        # Allow the test to interact with the page.
        yield page

    finally:
        # Close resources safely, even if a test fails.
        if context is not None:
            context.close()

        if browser is not None:
            browser.close()

        if playwright is not None:
            playwright.stop()
