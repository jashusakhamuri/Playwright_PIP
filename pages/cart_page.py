from locators.cart_locators import CartLocators
from utils.logger import get_logger


class CartPage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger("CartPage")

    def get_cart_title(self):

        self.logger.info("Getting cart page title")

        return self.page.locator(CartLocators.CART_TITLE).inner_text()

    def get_cart_product_name(self):

        self.logger.info("Getting cart product name")

        return self.page.locator(CartLocators.CART_PRODUCT_NAME).inner_text()

    def remove_product(self):

        self.logger.info("Removing product from cart")

        self.page.locator(CartLocators.REMOVE_PRODUCT).click()

    def is_product_visible(self):

        self.logger.info("Checking product visibility in cart")

        return self.page.locator(CartLocators.CART_PRODUCT_NAME).is_visible()