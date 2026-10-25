
"""
Shared Playwright helper functions for JE BikeZ automation.

Features:
- Element visibility and presence validation
- Click and input actions
- Text and attribute validation
- Checkbox and dropdown handling
- URL and page-title validation
- Waits, scrolling, and screenshots
- Consistent logging and observation delays
"""

import logging
from pathlib import Path
from typing import Callable, Optional, Union

from playwright.sync_api import (
    Locator,
    Page,
    TimeoutError as PlaywrightTimeoutError,
)

logger = logging.getLogger(__name__)

# -------------------- CONFIGURATION --------------------

DEFAULT_TIMEOUT = 20000
ELEMENT_VISIBILITY = 5000
ELEMENT_DISPLAY_WAIT = 500
SHORT_WAIT = 500
LONG_WAIT = 2000

SCREENSHOT_DIR = Path("screenshots")

LocatorType = Union[str, Locator]
LogCallback = Optional[Callable[[str, bool], None]]


class Helpers:
    """Reusable browser actions and validation helpers."""

    # -------------------- LOCATOR HANDLING --------------------

    @staticmethod
    def _get_locator(
        page: Page,
        locator: LocatorType,
        use_xpath: bool = False,
    ) -> Locator:
        """Convert a CSS/XPath string or Locator into a Playwright Locator."""
        if isinstance(locator, Locator):
            return locator

        if use_xpath:
            return page.locator(f"xpath={locator}")

        return page.locator(locator)

    @staticmethod
    def _record_result(
        description: str,
        passed: bool,
        log_result: LogCallback = None,
        message: str = "",
    ) -> bool:
        """Print and optionally report a validation result."""
        status = "PASS" if passed else "FAIL"
        details = f" - {message}" if message else ""

        print(f"{status}: {description}{details}")

        if log_result is not None:
            log_result(description, passed)

        if passed:
            logger.info("%s: %s%s", status, description, details)
        else:
            logger.error("%s: %s%s", status, description, details)

        return passed

    @staticmethod
    def _observe(page: Page, delay: int = ELEMENT_DISPLAY_WAIT) -> None:
        """Pause briefly so the user can observe the current action."""
        if delay > 0:
            page.wait_for_timeout(delay)

    # -------------------- VISIBILITY / PRESENCE --------------------

    @staticmethod
    def check_element_visibility(
        page: Page,
        locator: LocatorType,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = ELEMENT_VISIBILITY,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Wait for an element to become visible and report the result."""
        try:
            element = Helpers._get_locator(
                page, locator, use_xpath
            ).first

            element.wait_for(state="visible", timeout=timeout)

            passed = element.is_visible()

            Helpers._record_result(
                description,
                passed,
                log_result,
                "Element is visible" if passed else "Element is not visible",
            )

            Helpers._observe(page, observation_wait)
            return passed

        except PlaywrightTimeoutError:
            Helpers._record_result(
                description,
                False,
                log_result,
                f"Element did not become visible within {timeout} ms",
            )
            Helpers._observe(page, observation_wait)
            return False

        except Exception as error:
            Helpers._record_result(
                description,
                False,
                log_result,
                str(error),
            )
            Helpers._observe(page, observation_wait)
            return False

    @staticmethod
    def check_element_presence(
        page: Page,
        locator: LocatorType,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = ELEMENT_VISIBILITY,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Check that an element exists in the DOM, even if hidden."""
        try:
            element = Helpers._get_locator(
                page, locator, use_xpath
            ).first

            element.wait_for(state="attached", timeout=timeout)

            Helpers._record_result(
                description, True, log_result, "Element exists in DOM"
            )
            Helpers._observe(page, observation_wait)
            return True

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    @staticmethod
    def check_element_hidden(
        page: Page,
        locator: LocatorType,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = ELEMENT_VISIBILITY,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Validate that an element is hidden or detached."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.wait_for(state="hidden", timeout=timeout)

            Helpers._record_result(
                description, True, log_result, "Element is hidden"
            )
            Helpers._observe(page, observation_wait)
            return True

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    # -------------------- CLICK ACTIONS --------------------

    @staticmethod
    def click_element(
        page: Page,
        locator: LocatorType,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = DEFAULT_TIMEOUT,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Wait for an element, click it, and report the outcome."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.click(timeout=timeout)

            Helpers._record_result(
                description, True, log_result, "Click successful"
            )
            Helpers._observe(page, observation_wait)
            return True

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    # -------------------- INPUT ACTIONS --------------------

    @staticmethod
    def fill_input(
        page: Page,
        locator: LocatorType,
        value: str,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = DEFAULT_TIMEOUT,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Fill an input field with the provided value."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.fill(value, timeout=timeout)

            Helpers._record_result(
                description, True, log_result, "Input filled successfully"
            )
            Helpers._observe(page, observation_wait)
            return True

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    @staticmethod
    def type_text(
        page: Page,
        locator: LocatorType,
        value: str,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = DEFAULT_TIMEOUT,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Type text into an input using keyboard events."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.press_sequentially(value, timeout=timeout)

            Helpers._record_result(
                description, True, log_result, "Text typed successfully"
            )
            Helpers._observe(page, observation_wait)
            return True

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    # -------------------- TEXT VALIDATION --------------------

    @staticmethod
    def check_text(
        page: Page,
        locator: LocatorType,
        expected_text: str,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = ELEMENT_VISIBILITY,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Validate that an element's text contains the expected text."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.wait_for(state="visible", timeout=timeout)

            actual_text = element.inner_text(timeout=timeout).strip()
            passed = expected_text in actual_text

            Helpers._record_result(
                description,
                passed,
                log_result,
                f"Expected {expected_text!r}; actual {actual_text!r}",
            )
            Helpers._observe(page, observation_wait)
            return passed

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    @staticmethod
    def check_input_value(
        page: Page,
        locator: LocatorType,
        expected_value: str,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = ELEMENT_VISIBILITY,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Validate the current value of an input field."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.wait_for(state="visible", timeout=timeout)

            actual_value = element.input_value(timeout=timeout)
            passed = actual_value == expected_value

            Helpers._record_result(
                description,
                passed,
                log_result,
                f"Expected {expected_value!r}; actual {actual_value!r}",
            )
            Helpers._observe(page, observation_wait)
            return passed

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    # -------------------- ATTRIBUTE VALIDATION --------------------

    @staticmethod
    def check_attribute(
        page: Page,
        locator: LocatorType,
        attribute: str,
        expected_value: str,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = ELEMENT_VISIBILITY,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Validate an element's attribute value."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.wait_for(state="attached", timeout=timeout)

            actual_value = element.get_attribute(attribute)
            passed = actual_value == expected_value

            Helpers._record_result(
                description,
                passed,
                log_result,
                f"{attribute}: expected {expected_value!r}; actual {actual_value!r}",
            )
            Helpers._observe(page, observation_wait)
            return passed

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    # -------------------- CHECKBOX --------------------

    @staticmethod
    def check_checkbox(
        page: Page,
        locator: LocatorType,
        expected_checked: bool,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = DEFAULT_TIMEOUT,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Validate whether a checkbox is checked or unchecked."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.wait_for(state="visible", timeout=timeout)

            actual_checked = element.is_checked()
            passed = actual_checked == expected_checked

            Helpers._record_result(
                description,
                passed,
                log_result,
                f"Expected checked={expected_checked}; actual={actual_checked}",
            )
            Helpers._observe(page, observation_wait)
            return passed

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    @staticmethod
    def set_checkbox(
        page: Page,
        locator: LocatorType,
        checked: bool,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = DEFAULT_TIMEOUT,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Set a checkbox to the requested checked state."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first

            if checked:
                element.check(timeout=timeout)
            else:
                element.uncheck(timeout=timeout)

            Helpers._record_result(
                description, True, log_result, f"Checkbox set to {checked}"
            )
            Helpers._observe(page, observation_wait)
            return True

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    # -------------------- DROPDOWN --------------------

    @staticmethod
    def select_dropdown_option(
        page: Page,
        locator: LocatorType,
        value: str,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = DEFAULT_TIMEOUT,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Select a native dropdown option by its value."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.select_option(value, timeout=timeout)

            Helpers._record_result(
                description, True, log_result, f"Selected option {value!r}"
            )
            Helpers._observe(page, observation_wait)
            return True

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    # -------------------- URL / PAGE TITLE --------------------

    @staticmethod
    def check_url(
        page: Page,
        expected_url: str,
        description: str,
        log_result: LogCallback = None,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Validate the current browser URL."""
        actual_url = page.url
        passed = actual_url == expected_url

        Helpers._record_result(
            description,
            passed,
            log_result,
            f"Expected {expected_url!r}; actual {actual_url!r}",
        )
        Helpers._observe(page, observation_wait)
        return passed

    @staticmethod
    def check_url_contains(
        page: Page,
        expected_text: str,
        description: str,
        log_result: LogCallback = None,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Validate that the URL contains expected text."""
        actual_url = page.url
        passed = expected_text in actual_url

        Helpers._record_result(
            description,
            passed,
            log_result,
            f"Expected URL to contain {expected_text!r}; actual {actual_url!r}",
        )
        Helpers._observe(page, observation_wait)
        return passed

    @staticmethod
    def check_page_title(
        page: Page,
        expected_title: str,
        description: str,
        log_result: LogCallback = None,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Validate the browser page title."""
        try:
            actual_title = page.title()
            passed = actual_title == expected_title

            Helpers._record_result(
                description,
                passed,
                log_result,
                f"Expected {expected_title!r}; actual {actual_title!r}",
            )
            Helpers._observe(page, observation_wait)
            return passed

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    # -------------------- WAIT HELPERS --------------------

    @staticmethod
    def wait_for_element(
        page: Page,
        locator: LocatorType,
        state: str = "visible",
        timeout: int = DEFAULT_TIMEOUT,
        use_xpath: bool = False,
    ) -> bool:
        """Wait for an element state: attached, detached, visible, or hidden."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.wait_for(state=state, timeout=timeout)
            logger.info("Element reached state: %s", state)
            return True

        except Exception as error:
            logger.error("Element wait failed for state %s: %s", state, error)
            return False

    @staticmethod
    def wait_for_page_load(
        page: Page,
        state: str = "domcontentloaded",
        timeout: int = DEFAULT_TIMEOUT,
    ) -> bool:
        """Wait for a page lifecycle event."""
        try:
            page.wait_for_load_state(state=state, timeout=timeout)
            logger.info("Page reached load state: %s", state)
            return True

        except Exception as error:
            logger.error("Page load wait failed: %s", error)
            return False

    @staticmethod
    def wait(
        page: Page,
        milliseconds: int = SHORT_WAIT,
    ) -> None:
        """Explicit fixed delay when a test genuinely needs one."""
        Helpers._observe(page, milliseconds)

    # -------------------- SCROLLING --------------------

    @staticmethod
    def scroll_to_element(
        page: Page,
        locator: LocatorType,
        description: str,
        log_result: LogCallback = None,
        use_xpath: bool = False,
        timeout: int = DEFAULT_TIMEOUT,
        observation_wait: int = ELEMENT_DISPLAY_WAIT,
    ) -> bool:
        """Scroll an element into view."""
        try:
            element = Helpers._get_locator(page, locator, use_xpath).first
            element.scroll_into_view_if_needed(timeout=timeout)

            Helpers._record_result(
                description, True, log_result, "Scrolled element into view"
            )
            Helpers._observe(page, observation_wait)
            return True

        except Exception as error:
            Helpers._record_result(
                description, False, log_result, str(error)
            )
            Helpers._observe(page, observation_wait)
            return False

    # -------------------- SCREENSHOTS --------------------

    @staticmethod
    def take_screenshot(
        page: Page,
        filename: str = "screenshot.png",
        full_page: bool = True,
    ) -> Optional[str]:
        """Save a screenshot and return its path."""
        try:
            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
            path = SCREENSHOT_DIR / filename

            page.screenshot(
                path=str(path),
                full_page=full_page,
            )

            logger.info("Screenshot saved: %s", path)
            return str(path)

        except Exception as error:
            logger.error("Screenshot failed: %s", error)
            return None
