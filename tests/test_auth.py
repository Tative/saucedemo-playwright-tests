import pytest
from playwright.sync_api import Page, expect
from pages.login_page_pom import LoginPage
from logic.routes import Routes
from config import Config

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.goto()
    return lp

@pytest.mark.smoke
def test_valid_login(login_page: LoginPage) -> None:
    login_page.login(Config.USERNAME, Config.PASSWORD)
    expect(login_page.page).to_have_url(Routes.INVENTORY_URL)
    
@pytest.mark.regression
@pytest.mark.parametrize('username, password, error_message', [
    ('', Config.PASSWORD, 'Epic sadface: Username is required'),
    (Config.USERNAME, '', 'Epic sadface: Password is required'),
    ('invalid_user', 'invalid_password', 'Epic sadface: Username and password do not match any user in this service'),
    (Config.LOCKED_USER, Config.PASSWORD, 'Epic sadface: Sorry, this user has been locked out.')
])
def test_invalid_login(login_page: LoginPage, username: str, password: str, error_message: str) -> None:
    login_page.login(username, password) 
    expect(login_page.error_message).to_have_text(error_message)
    
