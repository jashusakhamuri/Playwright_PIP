from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.test_data_reader import load_test_data


# Load test data
test_data = load_test_data()


def test_open_cart(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    products_page.add_first_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(login_page.page)

    title = cart_page.get_cart_title()

    assert title == test_data["expected"]["cart"]["title"]


def test_product_appears_in_cart(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    products_page.add_first_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(login_page.page)

    product_name = cart_page.get_cart_product_name()

    assert (
        product_name
        == test_data["expected"]["cart"]["product_name"]
    )


def test_remove_product_from_cart(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    products_page = ProductsPage(login_page.page)

    products_page.add_first_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(login_page.page)

    cart_page.remove_product()

    product_visible = cart_page.is_product_visible()

    assert product_visible is False