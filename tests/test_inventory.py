import pytest
from playwright.sync_api import Page, expect
from logic.flow import Flow
from logic.routes import Routes
import allure


@pytest.fixture
def auth_flow(page: Page) -> Flow:
    flow = Flow(page)
    flow.authenticate()
    return flow


@allure.title("Добавление двух товаров обновляет бейдж корзины")
@pytest.mark.regression
def test_add_two_items_shows_cart_badge(auth_flow: Flow) -> None:
    auth_flow.inventory_page.add_items()
    
    with allure.step("Проверка: отображения цифры '2' на бейдже корзины"):
        expect(auth_flow.inventory_page.cart_badge).to_have_text("2")


@allure.title("В корзине отображается два товара после их добавления")
@pytest.mark.smoke
def test_add_items_and_go_to_cart(auth_flow: Flow) -> None:
    auth_flow.add_items_and_go_to_cart()
    
    with allure.step("Проверка: URL -> /cart.html, количества товаров в корзине = 2"):
        expect(auth_flow.page).to_have_url(Routes.CART_URL)
        expect(auth_flow.inventory_page.cart_items).to_have_count(2)


@allure.title("Удаление одного товара из корзины")
@pytest.mark.regression
def test_remove_one_item_updates_cart_badge(auth_flow: Flow) -> None:
    auth_flow.inventory_page.add_items()
    auth_flow.inventory_page.remove_backpack_from_cart()
    
    with allure.step("Проверка: бейдж отображает цифру '1'"):
        expect(auth_flow.inventory_page.cart_badge).to_have_text("1")
