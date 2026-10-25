from playwright.sync_api import expect

class Verification:
    @staticmethod
    def visible(locator) -> None:
        expect(locator).to_be_visible()

    @staticmethod
    def text(locator, expected_text: str) -> None:
        expect(locator).to_contain_text(expected_text)

    @staticmethod
    def url(page, expected_url: str) -> None:
        expect(page).to_have_url(expected_url)

    @staticmethod
    def page_loaded(page) -> None:
        expect(page.locator("body")).to_be_visible()
