from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from utils.test_data_reader import load_test_data


# Load test data
test_data = load_test_data()


def open_checkout(login_page):

    # Login
    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    products_page.add_first_product_to_cart()

    products_page.open_cart()

    checkout_page = CheckoutPage(login_page.page)

    checkout_page.click_checkout()

    return checkout_page

def test_open_checkout(login_page):

    checkout_page = open_checkout(login_page)

    title = checkout_page.get_checkout_title()

    assert (
        title
        == test_data["expected"]["checkout"]["information_title"]
    )


def test_checkout_with_valid_information(login_page):

    checkout_page = open_checkout(login_page)

    checkout_page.enter_first_name(
        test_data["checkout"]["valid"]["first_name"]
    )

    checkout_page.enter_last_name(
        test_data["checkout"]["valid"]["last_name"]
    )

    checkout_page.enter_postal_code(
        test_data["checkout"]["valid"]["postal_code"]
    )

    checkout_page.click_continue()

    overview_title = checkout_page.get_overview_title()

    assert (
        overview_title
        == test_data["expected"]["checkout"]["overview_title"]
    )

def test_checkout_without_first_name(login_page):

    checkout_page = open_checkout(login_page)

    checkout_page.enter_last_name(
        test_data["checkout"]["valid"]["last_name"]
    )

    checkout_page.enter_postal_code(
        test_data["checkout"]["valid"]["postal_code"]
    )

    checkout_page.click_continue()

    error_message = checkout_page.get_error_message()

    assert (
        error_message
        == test_data["expected"]["checkout"]["first_name_error"]
    )

def test_checkout_without_last_name(login_page):

    checkout_page = open_checkout(login_page)

    checkout_page.enter_first_name(
        test_data["checkout"]["valid"]["first_name"]
    )

    checkout_page.enter_postal_code(
        test_data["checkout"]["valid"]["postal_code"]
    )

    checkout_page.click_continue()

    error_message = checkout_page.get_error_message()

    assert (
        error_message
        == test_data["expected"]["checkout"]["last_name_error"]
    )


def test_checkout_without_postal_code(login_page):

    checkout_page = open_checkout(login_page)

    checkout_page.enter_first_name(
        test_data["checkout"]["valid"]["first_name"]
    )

    checkout_page.enter_last_name(
        test_data["checkout"]["valid"]["last_name"]
    )

    checkout_page.click_continue()

    error_message = checkout_page.get_error_message()

    assert (
        error_message
        == test_data["expected"]["checkout"]["postal_code_error"]
    )


def test_verify_product_in_checkout_overview(login_page):

    checkout_page = open_checkout(login_page)

    checkout_page.enter_first_name(
        test_data["checkout"]["valid"]["first_name"]
    )

    checkout_page.enter_last_name(
        test_data["checkout"]["valid"]["last_name"]
    )

    checkout_page.enter_postal_code(
        test_data["checkout"]["valid"]["postal_code"]
    )

    checkout_page.click_continue()

    product_name = checkout_page.get_product_name()

    product_price = checkout_page.get_product_price()

    assert (
        product_name
        == test_data["expected"]["checkout"]["product_name"]
    )

    assert (
        product_price
        == test_data["expected"]["checkout"]["product_price"]
    )


def test_complete_checkout(login_page):

    checkout_page = open_checkout(login_page)

    checkout_page.enter_first_name(
        test_data["checkout"]["valid"]["first_name"]
    )

    checkout_page.enter_last_name(
        test_data["checkout"]["valid"]["last_name"]
    )

    checkout_page.enter_postal_code(
        test_data["checkout"]["valid"]["postal_code"]
    )

    checkout_page.click_continue()

    checkout_page.click_finish()

    complete_title = checkout_page.get_complete_title()

    assert (
        complete_title
        == test_data["expected"]["checkout"]["complete_title"]
    )