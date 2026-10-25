# """
# JE BikeZ - Home Page Validation Functions.
# """

# from playwright.sync_api import Page

# from web_automation.locators.home_locator import HomeLocators
# from web_automation.utils.helpers import Helpers


# def _check_home_page_validation(page: Page, log_result) -> None:
#     """
#     Validate the homepage elements.

#     Each visibility check uses the default 2-second timeout defined
#     in utils/helpers.py.
#     """
#     page.wait_for_load_state(
#         "domcontentloaded",
#         timeout=5000,
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.HOME_PAGE_SECTION,
#         description="Validate Home Page Section",
#         log_result=log_result,
#         timeout=5000
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.NAV_MANU,
#         description="Validate Navigation Menu",
#         log_result=log_result,
#         timeout=5000
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.JE_LOGO,
#         description="Validate JE BikeZ Logo",
#         log_result=log_result,
#         timeout=5000
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.HOME_BUTTON,
#         description="Validate Home Navigation Button",
#         log_result=log_result,
#         timeout=5000
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.SERVICE_BUTTON,
#         description="Validate Services Navigation Button",
#         log_result=log_result,
#         timeout=5000
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.BUILD_BUTTON,
#         description="Validate Builds Navigation Button",
#         log_result=log_result,
#         timeout=5000
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.SALES_BUTTON,
#         description="Validate Sales Navigation Button",
#         log_result=log_result,
#         timeout=5000
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.ABOUTUS_BUTTON,
#         description="Validate About Us Navigation Button",
#         log_result=log_result,
#         timeout=5000
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.CONTACT_BUTTON,
#         description="Validate Contact Navigation Button",
#         log_result=log_result,
#         timeout=5000
#     )

#     Helpers.check_element_visibility(
#         page=page,
#         locator=HomeLocators.LOGIN_SIGNUP_BUTTON,
#         description="Validate Login / Signup Button",
#         log_result=log_result,
#         timeout=5000
#     )   

#     # checks = [
#     #     (
#     #         HomeLocators.HOME_PAGE_SECTION,
#     #         "Validate Home Page Section",
#     #     ),
#     #     (
#     #         HomeLocators.NAV_MANU,
#     #         "Validate Navigation Menu",
#     #     ),
#     #     (
#     #         HomeLocators.JE_LOGO,
#     #         "Validate JE BikeZ Logo",
#     #     ),
#     #     (
#     #         HomeLocators.HOME_BUTTON,
#     #         "Validate Home Navigation Button",
#     #     ),
#     #     (
#     #         HomeLocators.SERVICE_BUTTON,
#     #         "Validate Services Navigation Button",
#     #     ),
#     #     (
#     #         HomeLocators.BUILD_BUTTON,
#     #         "Validate Builds Navigation Button",
#     #     ),
#     #     (
#     #         HomeLocators.SALES_BUTTON,
#     #         "Validate Sales Navigation Button",
#     #     ),
#     #     (
#     #         HomeLocators.ABOUTUS_BUTTON,
#     #         "Validate About Us Navigation Button",
#     #     ),
#     #     (
#     #         HomeLocators.CONTACT_BUTTON,
#     #         "Validate Contact Navigation Button",
#     #     ),
#     #     (
#     #         HomeLocators.LOGIN_SIGNUP_BUTTON,
#     #         "Validate Login / Signup Button",
#     #     ),
#     # ]

#     # for locator, description in checks:
#     #     Helpers.check_element_visibility(
#     #         page=page,
#     #         locator=locator,
#     #         description=description,
#     #         log_result=log_result,
#     #     )






from playwright.sync_api import Page
from web_automation.locators.home_locator import HomeLocators
from web_automation.utils.helpers import Helpers


def _check_home_page_validation(page: Page, log_result) -> None:
    page.wait_for_load_state("domcontentloaded", timeout=15000)

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.HOME_PAGE_SECTION,
        description="Validate Home Page Section",
        log_result=log_result,
        timeout=5000
    )

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.NAV_MANU,
        description="Validate Navigation Menu",
        log_result=log_result,
        timeout=5000
    )

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.JE_LOGO,
        description="Validate JE BikeZ Logo",
        log_result=log_result,
        timeout=5000
    )

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.HOME_BUTTON,
        description="Validate Home Navigation Button",
        log_result=log_result,
        timeout=5000
    )

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.SERVICE_BUTTON,
        description="Validate Services Navigation Button",
        log_result=log_result,
        timeout=5000
    )

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.BUILD_BUTTON,
        description="Validate Builds Navigation Button",
        log_result=log_result,
        timeout=5000
    )

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.SALES_BUTTON,
        description="Validate Sales Navigation Button",
        log_result=log_result,
        timeout=5000
    )

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.ABOUTUS_BUTTON,
        description="Validate About Us Navigation Button",
        log_result=log_result,
        timeout=5000
    )

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.CONTACT_BUTTON,
        description="Validate Contact Navigation Button",
        log_result=log_result,
        timeout=5000
    )

    Helpers.check_element_visibility(
        page=page,
        locator=HomeLocators.LOGIN_SIGNUP_BUTTON,
        description="Validate Login / Signup Button",
        log_result=log_result,
        timeout=5000
    )