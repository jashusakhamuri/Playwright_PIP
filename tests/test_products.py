from pages.products_page import ProductsPage
from utils.test_data_reader import load_test_data


# Load test data
test_data = load_test_data()


def test_products_page(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    title = products_page.get_product_title()

    assert title == test_data["expected"]["products"]["title"]


def test_add_first_product_to_cart(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    products_page.add_first_product_to_cart()

    cart_count = products_page.get_cart_count()

    assert cart_count == test_data["expected"]["products"]["cart_count"]


def test_remove_first_product_from_cart(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    products_page.add_first_product_to_cart()

    products_page.remove_first_product()

    cart_visible = products_page.is_cart_count_visible()

    assert cart_visible is False


def test_open_first_product(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    products_page.click_first_product()

    product_title = products_page.get_product_details_title()

    assert product_title == test_data["expected"]["products"]["product_name"]


def test_sort_products_a_to_z(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    products_page.sort_products(
        test_data["expected"]["sorting"]["name_ascending"]
    )

    product_names = products_page.get_all_product_names()

    assert product_names == sorted(product_names)


def test_sort_products_price_low_to_high(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    products_page.sort_products(
        test_data["expected"]["sorting"]["price_low_to_high"]
    )

    prices = products_page.get_all_product_prices()

    prices = [
        float(price.replace("$", ""))
        for price in prices
    ]

    assert prices == sorted(prices)