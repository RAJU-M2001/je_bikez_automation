
from typing import Optional


class HomeLocators:
    """Locators for the JE BikeZ Home page."""
    # test

    HOME_PAGE_SECTION = "//section[@class='section top-section pt-100']"
    NAV_MANU = "//div[@class='navbar-container']"
    JE_LOGO = "//a[@class='logo']//img[@alt='JE BikeZ']"

    HOME_BUTTON = "(//a[@class='active'])[1]"
    SERVICE_BUTTON = (
        "//nav[@id='navLinks']//a[@href='service.html']"
        "[normalize-space()='Services']"
    )
    BUILD_BUTTON = (
        "//nav[@id='navLinks']//a[@href='builds.html']"
        "[normalize-space()='Builds']"
    )
    SALES_BUTTON = (
        "//nav[@id='navLinks']//a[@href='sales.html']"
        "[normalize-space()='Sales']"
    )
    ABOUTUS_BUTTON = "//a[normalize-space()='About Us']"
    CONTACT_BUTTON = "//a[contains(text(),'Contact')]"
    LOGIN_SIGNUP_BUTTON = "//button[@id='loginSignupBtn']"
