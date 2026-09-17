from locators.checkout_locators import CheckoutLocators
from utils.logger import get_logger


class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger("CheckoutPage")

    def click_checkout(self):

        self.logger.info("Clicking checkout button")

        self.page.locator(CheckoutLocators.CHECKOUT_BUTTON).click()

    def get_checkout_title(self):

        self.logger.info("Getting checkout page title")

        return self.page.locator(CheckoutLocators.CHECKOUT_TITLE).inner_text()

    def enter_first_name(self, first_name):

        self.logger.info("Entering first name")

        self.page.locator(CheckoutLocators.FIRST_NAME).fill(first_name)

    def enter_last_name(self, last_name):

        self.logger.info("Entering last name")

        self.page.locator(CheckoutLocators.LAST_NAME).fill(last_name)

    def enter_postal_code(self, postal_code):

        self.logger.info("Entering postal code")

        self.page.locator(CheckoutLocators.POSTAL_CODE).fill(postal_code)

    def click_continue(self):

        self.logger.info("Clicking continue button")

        self.page.locator(CheckoutLocators.CONTINUE_BUTTON).click()

    def get_error_message(self):

        self.logger.info("Getting checkout error message")

        return self.page.locator(CheckoutLocators.ERROR_MESSAGE).inner_text()

    def get_overview_title(self):

        self.logger.info("Getting checkout overview title")

        return self.page.locator(CheckoutLocators.OVERVIEW_TITLE).inner_text()

    def get_product_name(self):

        self.logger.info("Getting product name")

        return self.page.locator(CheckoutLocators.PRODUCT_NAME).inner_text()

    def get_product_price(self):

        self.logger.info("Getting product price")

        return self.page.locator(CheckoutLocators.PRODUCT_PRICE).inner_text()

    def click_finish(self):

        self.logger.info("Clicking finish button")

        self.page.locator(CheckoutLocators.FINISH_BUTTON).click()

    def get_complete_title(self):

        self.logger.info("Getting order completion message")

        return self.page.locator(CheckoutLocators.COMPLETE_TITLE).inner_text()