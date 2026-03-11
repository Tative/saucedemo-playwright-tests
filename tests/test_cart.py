import pytest
from playwright.sync_api import Page, expect
from logic.flow import Flow
from decimal import Decimal
from logic.routes import Routes
import allure


@pytest.fixture
def user_in_cart(page: Page) -> Flow:
    flow = Flow(page)
    flow.authenticate()
    flow.add_items_and_go_to_cart()
    return flow

@allure.title("Общая стоимость товаров в корзине")   
@pytest.mark.regression
def test_full_price(user_in_cart: Flow) -> None:
    with allure.step("Получение общей стоимости товаров в корзине"):
        full_price = user_in_cart.cart_page.get_full_price()
    
    with allure.step(f"Проверка, что отображаемая общая стоимость равна {full_price}"):
        assert full_price == Decimal('39.98')


@allure.title("Удаление одного товара из корзины") 
@pytest.mark.regression
def test_remove_item(user_in_cart: Flow) -> None:
    user_in_cart.cart_page.remove_item('Backpack')
    
    with allure.step("Получение общей стоимости после удаления товара"):
        full_price = user_in_cart.cart_page.get_full_price()
    
    with allure.step("Проверка: удаление одного товара обновляет общую стоимость в корзине"):
        assert full_price == Decimal('9.99')
    
    
@allure.title("Удаление всех товаров из корзины")        
@pytest.mark.regression
def test_remove_all_items(user_in_cart: Flow) -> None:
    user_in_cart.cart_page.remove_all()
    
    with allure.step("Проверка: корзина пуста и товары не отображаются"):
        expect(user_in_cart.cart_page.cart_item).not_to_be_visible()
   
    
@allure.title("Кнопка 'Continue Shopping' возвращает на страницу инвентаря")     
@pytest.mark.regression 
def test_continue_button(user_in_cart: Flow) -> None:
    user_in_cart.cart_page.go_to_continue_shopping()
    
    with allure.step("Проверка: URL -> /inventory.html после нажатия кнопки 'Continue Shopping'"):
        expect(user_in_cart.page).to_have_url(Routes.INVENTORY_URL)
    
    
@allure.title("Кнопка 'Checkout' направляет на страницу оформления заказа")     
@pytest.mark.smoke   
def test_checkout_button(user_in_cart: Flow) -> None:
    user_in_cart.cart_page.go_to_checkout()
    
    with allure.step("Проверка: URL -> /checkout.html после нажатия кнопки 'Checkout'"):
        expect(user_in_cart.page).to_have_url(Routes.CHECKOUT_URL)
    



    