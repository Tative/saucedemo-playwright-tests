import pytest
from playwright.sync_api import Page, expect
from pages.login_page_pom import LoginPage
from logic.routes import Routes
from config import Config
from loguru import logger
import allure


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.goto()
    return lp


@allure.title("Успешная авторизация")
@pytest.mark.smoke
def test_valid_login(login_page: LoginPage) -> None:
    login_page.login(Config.USER_NAME, Config.PASSWORD)
    
    with allure.step("Проверка: URL -> /inventory.html после успешной авторизации"):
        expect(login_page.page).to_have_url(Routes.INVENTORY_URL)
    
    
@allure.title("Различные сценарии неуспешной авторизации")
@pytest.mark.regression
@pytest.mark.parametrize('username, password, error_message', [
    ('', 'any_password', 'Epic sadface: Username is required'),
    (Config.USER_NAME, '', 'Epic sadface: Password is required'),
    ('invalid_user', 'invalid_password', 'Epic sadface: Username and password do not match any user in this service')
    ])
def test_invalid_login(login_page: LoginPage, username: str, password: str, error_message: str) -> None:
    allure.dynamic.title(f"Неуспешная авторизация: '{error_message}'")
    login_page.login(username, password)
    
    with allure.step(f"Проверка ошибки: '{error_message}'"):
       expect(login_page.error_message).to_have_text(error_message)
    
    
@allure.title("Заблокированный пользователь не может войти")
@pytest.mark.regression
def test_locked_user_login(login_page: LoginPage) -> None:
    login_page.login(Config.LOCKED_USER, Config.PASSWORD)
    
    with allure.step("Проверка ошибки о блокировке"):
        expect(login_page.error_message).to_have_text(
            'Epic sadface: Sorry, this user has been locked out.')