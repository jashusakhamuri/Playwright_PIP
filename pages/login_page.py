from locators.login_locators import LoginLocators
from utils.logger import get_logger


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger("LoginPage")

    def enter_username(self, username):

        self.logger.info("Entering username")

        self.page.locator(LoginLocators.USERNAME).fill(username)

    def enter_password(self, password):

        self.logger.info("Entering password")

        self.page.locator(LoginLocators.PASSWORD).fill(password)

    def click_login(self):

        self.logger.info("Clicking login button")

        self.page.locator(LoginLocators.LOGIN_BUTTON).click()

    def login(self, username, password):

        self.logger.info("Login started")

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        self.logger.info("Login completed")

    def get_error_message(self):

        self.logger.info("Getting login error message")

        return self.page.locator(LoginLocators.ERROR_MESSAGE).inner_text()