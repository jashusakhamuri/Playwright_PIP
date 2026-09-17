from utils.test_data_reader import load_test_data


# Load test data
test_data = load_test_data()


def test_valid_login(login_page):

    login_page.login(
        test_data["users"]["standard_user"]["username"],
        test_data["users"]["standard_user"]["password"]
    )

    assert login_page.page.url == test_data["expected"]["inventory_url"]


def test_invalid_login(login_page):

    login_page.login(
        test_data["users"]["invalid_user"]["username"],
        test_data["users"]["invalid_user"]["password"]
    )

    error_message = login_page.get_error_message()

    assert (
        test_data["expected"]["login_errors"]["invalid_credentials"]
        in error_message
    )


def test_empty_username(login_page):

    login_page.enter_password(
        test_data["users"]["standard_user"]["password"]
    )

    login_page.click_login()

    error_message = login_page.get_error_message()

    assert (
        test_data["expected"]["login_errors"]["empty_username"]
        in error_message
    )


def test_empty_password(login_page):

    login_page.enter_username(
        test_data["users"]["standard_user"]["username"]
    )

    login_page.click_login()

    error_message = login_page.get_error_message()

    assert (
        test_data["expected"]["login_errors"]["empty_password"]
        in error_message
    )


def test_locked_out_user(login_page):

    login_page.login(
        test_data["users"]["locked_out_user"]["username"],
        test_data["users"]["locked_out_user"]["password"]
    )

    error_message = login_page.get_error_message()

    assert (
        test_data["expected"]["login_errors"]["locked_out"]
        in error_message
    )