"""
JE BikeZ - Home Page Automation Test Entry Point.
"""

import logging
from typing import Optional

from playwright.sync_api import Page

from web_automation.config.config import get_base_url
from web_automation.core.browser import browser_page
from web_automation.pages.home_page import _check_home_page_validation
from web_automation.utils.report import log_test_case

logger = logging.getLogger(__name__)


def _execute_home_page_test(page: Page) -> None:
    """Navigate to the homepage and run all homepage validations."""

    failed_cases = []

    def log_result(description: str, passed: bool) -> None:
        """Record one validation in the shared report results."""
        status = "PASSED" if passed else "FAILED"

        message = (
            "Element is visible."
            if passed
            else "Element was not visible within the configured timeout."
        )

        log_test_case(
            test_name="Home",
            test_case=description,
            status=status,
            message=message,
        )

        if passed:
            logger.info("PASS: %s", description)
        else:
            logger.error("FAIL: %s", description)
            failed_cases.append(description)

    base_url = get_base_url()

    if not base_url:
        raise RuntimeError(
            "The JE BikeZ base URL is empty. Check your configuration."
        )

    logger.info("Opening JE BikeZ homepage: %s", base_url)

    # Navigate to the application before checking page elements.
    try:
        response = page.goto(
            base_url,
            wait_until="domcontentloaded",
            timeout=60000,
        )
        page.wait_for_timeout(5000)
    except Exception as error:
        log_result("Home Page URL Launch", False)
        raise AssertionError(
            f"Could not navigate to {base_url}: {error}"
        ) from error

    # Record HTTP navigation result.
    log_result(
        "Home Page URL Launch",
        response is not None and response.status < 400,
    )

    # Record final browser URL result.
    log_result(
        "Home Page URL Is Valid",
        page.url.startswith(("http://", "https://")),
    )

    # The element-level test cases are implemented in home_page.py.
    _check_home_page_validation(page, log_result)

    # Raise only after all element checks have been attempted.
    if failed_cases:
        raise AssertionError(
            f"Home page test failed: {len(failed_cases)} validation(s). "
            f"Failed cases: {', '.join(failed_cases)}"
        )

    logger.info("All homepage validations passed.")


def check_home_page(page: Optional[Page] = None) -> None:
    """
    Entry point used by main.py.

    Reuse the runner-provided Page. If called directly without a Page,
    create a standalone browser using browser_page().
    """
    if page is not None:
        _execute_home_page_test(page)
        return

    with browser_page() as standalone_page:
        _execute_home_page_test(standalone_page)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
    )
    check_home_page()
