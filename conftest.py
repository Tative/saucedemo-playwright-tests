import pytest
from playwright.sync_api import Playwright
import allure


@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        page = None
        if 'page' in item.funcargs:
            page = item.funcargs['page']
        elif 'user_in_checkout' in item.funcargs:
            page = item.funcargs['user_in_checkout'].page
        
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="Скриншот ошибки",
                attachment_type=allure.attachment_type.PNG
            )
