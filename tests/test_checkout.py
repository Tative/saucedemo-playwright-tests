import pytest
from playwright.sync_api import Page, expect
from logic.flow import Flow
from logic.routes import Routes
from config import Config
import allure


@pytest.fixture
def user_in_checkout(page: Page) -> Flow:
    flow = Flow(page)
    flow.authenticate()
    flow.add_items_and_go_to_cart()
    flow.go_to_checkout()
    return flow


@allure.title("Текст ошибки отображается корректно в зависимости от введенных данных")
@pytest.mark.regression
@pytest.mark.parametrize("first_name, last_name, zip_postal, error", [
    ('', 'test_last_name', 'test_postal_code', 'Error: First Name is required'),
    ('test_first_name', '', 'test_postal_code', 'Error: Last Name is required'),
    ('test_first_name', 'test_last_name', '', 'Error: Postal Code is required')
])
def test_invalid_info(user_in_checkout: Flow, first_name: str,
                      last_name: str, zip_postal: str, error: str) -> None:
    user_in_checkout.checkout_page.input_info(first_name, last_name, zip_postal)
    user_in_checkout.checkout_page.go_to_continue()
    
    with allure.step("Проверка отображения соответствующей ошибки"):
        expect(user_in_checkout.checkout_page.error).to_have_text(error)
    
    
@allure.title("Кнопка 'Cancel' возвращает на страницу инвентаря")
@pytest.mark.smoke   
def test_cancel_button(user_in_checkout: Flow) -> None:
    user_in_checkout.checkout_page.go_to_cancel()
    with allure.step("Проверка: URL -> /inventory.html после нажатия кнопки 'Cancel'"):
        # expect(user_in_checkout.page).to_have_url(Routes.CART_URL) это строка правильная.
        expect(user_in_checkout.page).to_have_url(Routes.INVENTORY_URL) # это намеренная ошибка для алюра. потом надо изменить обратно


@allure.title("Кнопка 'Continue' направляет на страницу обзора заказа")
@pytest.mark.smoke
def test_valid_info(user_in_checkout: Flow) -> None:
    user_in_checkout.checkout_page.input_info(Config.FIRST_NAME, Config.LAST_NAME, Config.POSTAL_CODE)
    user_in_checkout.checkout_page.go_to_continue()
    
    with allure.step("Проверка: URL -> /checkout-overview.html после ввода валидных данных и нажатия кнопки 'Continue'"):
        expect(user_in_checkout.page).to_have_url(Routes.CHECKOUT_OVERVIEW_URL)