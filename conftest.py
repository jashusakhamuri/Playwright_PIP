import pytest
from pathlib import Path
from playwright.sync_api import Page

from utils.config_reader import load_config
from pages.login_page import LoginPage


# Screenshot folder
SCREENSHOT_DIR = (
    Path(__file__).parent / "screenshots"
)

SCREENSHOT_DIR.mkdir(exist_ok=True)


@pytest.fixture
def login_page(page: Page):
    config = load_config()

    page.goto(config["base_url"])

    return LoginPage(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Execute the actual test first
    outcome = yield

    # Get test result
    report = outcome.get_result()

    # Take screenshot only when the test fails
    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            screenshot_path = (
                SCREENSHOT_DIR
                / f"{item.name}.png"
            )

            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )

            print(
                f"\nScreenshot saved: {screenshot_path}"
            )