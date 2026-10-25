"""
JE BikeZ - Custom Playwright Test Runner.

Example runner for the Home test. Preserve other test registrations
from your existing runner when integrating this implementation.
"""

import argparse
import logging
import time

from web_automation.core.browser import browser_page
from web_automation.tests.test_home_page import check_home_page
from web_automation.utils.report import (
    get_logger,
    reset_test_case_results,
    save_html_report,
    save_test_report,
)

logger = get_logger("web_automation")


def run_test(test_name: str) -> dict:
    """Run the selected test and return its overall result."""

    test_functions = {
        "home": check_home_page,
    }

    if test_name not in test_functions:
        raise ValueError(
            f"Unknown test '{test_name}'. "
            f"Available tests: {', '.join(test_functions)}"
        )

    test_function = test_functions[test_name]
    started = time.perf_counter()

    result = {
        "test_name": test_name,
        "status": "PASSED",
        "message": "",
    }

    logger.info("Starting test: %s", test_name)

    try:
        with browser_page() as page:
            test_function(page)

    except Exception as error:
        result["status"] = "FAILED"
        result["message"] = str(error)
        logger.exception("Test failed: %s", test_name)

    result["duration"] = round(time.perf_counter() - started, 2)

    logger.info(
        "%s: %s",
        result["status"],
        test_name,
    )

    return result


def main() -> int:
    """Run tests and generate the Excel and HTML reports."""

    parser = argparse.ArgumentParser(
        description="JE BikeZ Playwright Automation Runner"
    )
    parser.add_argument(
        "--test",
        default="home",
        help="Test name to run, for example:home",
    )
    args = parser.parse_args()

    reset_test_case_results()

    overall_started = time.perf_counter()
    results = [run_test(args.test)]
    total_duration = time.perf_counter() - overall_started

    excel_path = save_test_report(
        results,
        total_duration=total_duration,
    )
    html_path = save_html_report(
        results,
        total_duration=total_duration,
    )

    print("\n========== JE BikeZ Test Summary ==========")
    print(f"Passed: {sum(r['status'] == 'PASSED' for r in results)}")
    print(f"Failed: {sum(r['status'] == 'FAILED' for r in results)}")
    print(f"Excel report: {excel_path}")
    print(f"HTML report:  {html_path}")
    print("===========================================\n")

    return 1 if any(r["status"] == "FAILED" for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
