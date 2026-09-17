from locators.products_locators import ProductLocators
from utils.logger import get_logger


class ProductsPage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger("ProductsPage")

    def get_product_title(self):

        self.logger.info("Getting products page title")

        return self.page.locator(ProductLocators.PRODUCTS_TITLE).inner_text()

    def click_first_product(self):

        self.logger.info("Clicking first product")

        self.page.locator(ProductLocators.FIRST_PRODUCT).click()

    def add_first_product_to_cart(self):

        self.logger.info("Adding first product to cart")

        self.page.locator(ProductLocators.ADD_TO_CART).click()

    def remove_first_product(self):

        self.logger.info("Removing first product from cart")

        self.page.locator(ProductLocators.REMOVE).click()

    def open_cart(self):

        self.logger.info("Opening shopping cart")

        self.page.locator(ProductLocators.CART_ICON).click()

    def sort_products(self, value):

        self.logger.info(f"Sorting products using value: {value}")

        self.page.locator(ProductLocators.SORT_DROPDOWN).select_option(value)

    def get_cart_count(self):

        self.logger.info("Getting cart item count")

        return self.page.locator(ProductLocators.CART_COUNT).inner_text()

    def is_cart_count_visible(self):

        self.logger.info("Checking cart count visibility")

        return self.page.locator(ProductLocators.CART_COUNT).is_visible()

    def get_product_details_title(self):

        self.logger.info("Getting product details title")

        return self.page.locator(ProductLocators.PRODUCT_DETAILS_TITLE).inner_text()

    def get_all_product_names(self):

        self.logger.info("Getting all product names")

        return self.page.locator(ProductLocators.PRODUCT_NAMES).all_inner_texts()

    def get_all_product_prices(self):

        self.logger.info("Getting all product prices")

        return self.page.locator(ProductLocators.PRODUCT_PRICES).all_inner_texts()