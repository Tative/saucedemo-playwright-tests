import pytest
from playwright.sync_api import Page, expect
from logic.flow import Flow
from logic.routes import Routes
import allure


@pytest.fixture
def user_in_overview(page: Page) -> Flow:
    flow = Flow(page)
    flow.authenticate()
    flow.add_items_and_go_to_cart()
    flow.go_to_checkout()
    flow.go_to_checkout_overview()
    return flow

    
@allure.title("Кнопка 'Cancel' возвращает на страницу инвентаря")
@pytest.mark.smoke 
def test_cancel_button(user_in_overview: Flow) -> None:
    user_in_overview.checkout_overview_page.go_to_cancel()
    
    with allure.step("Проверка URL -> /inventory.html после нажатия кнопки 'Cancel'"):
        expect(user_in_overview.page).to_have_url(Routes.INVENTORY_URL)


@allure.title("Кнопка 'Finish' направляет на страницу завершения заказа")
@pytest.mark.smoke 
def test_finish_button(user_in_overview: Flow) -> None:
    user_in_overview.checkout_overview_page.go_to_finish()
    
    with allure.step("Проверка URL -> /finish.html после нажатия кнопки 'Finish'"):
        expect(user_in_overview.page).to_have_url(Routes.FINISH_URL)


@allure.title("Сумма налога отображается корректно")
@pytest.mark.smoke 
def test_tax_price(user_in_overview: Flow) -> None:
    with allure.step("Получение ожидаемой суммы налога"):
        expected_tax = user_in_overview.checkout_overview_page.get_tax_price()
    
    with allure.step(f"Проверка: сумма налога соответствует {expected_tax}"):
        expect(user_in_overview.checkout_overview_page.tax_price).to_contain_text(str(expected_tax))


@allure.title("Сумма заказа без налога отображается корректно")
@pytest.mark.smoke 
def test_subtotal_price(user_in_overview: Flow) -> None:
    with allure.step("Получение ожидаемой суммы заказа без налога"):
        subtotal_expected = user_in_overview.checkout_overview_page.get_subtotal_price()
    
    with allure.step(f"Проверка: сумма заказа без налога соответствует {subtotal_expected}"):
        expect(user_in_overview.checkout_overview_page.subtotal_price).to_contain_text(str(subtotal_expected))

 
@allure.title("Сумма заказа отображается корректно")   
@pytest.mark.smoke 
def test_total_price(user_in_overview: Flow) -> None:
    with allure.step("Получение ожидаемой общей суммы заказа"):
        total_expected = user_in_overview.checkout_overview_page.get_total_price()
    
    with allure.step(f"Проверка: общая сумма заказа соответствует {total_expected}"):
        expect(user_in_overview.checkout_overview_page.total_price).to_contain_text(str(total_expected))
   
 
@allure.title("Тест на количество товаров в корзине")
@pytest.mark.regression 
def test_items_in_cart(user_in_overview: Flow) -> None:
    with allure.step("Проверка: количество товаров в корзине равно 2"):
        expect(user_in_overview.checkout_overview_page.cart_item).to_have_count(2)
    
    
    