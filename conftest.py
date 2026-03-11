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
        
        for fixture_value in item.funcargs.values():
            if hasattr(fixture_value, 'screenshot'):  # это Page объект
                page = fixture_value
                break
            if hasattr(fixture_value, 'page') and hasattr(fixture_value.page, 'screenshot'):  # это Flow объект
                page = fixture_value.page
                break
        
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="Скриншот ошибки",
                attachment_type=allure.attachment_type.PNG
            )