import pytest
from playwright.sync_api import Page, expect
from logic.flow import Flow
from decimal import Decimal
from logic.routes import Routes


@pytest.fixture
def user_in_cart(page: Page) -> Flow:
    flow = Flow(page)
    flow.authenticate()
    flow.add_items_and_go_to_cart()
    return flow
    
    
@pytest.mark.regression
def test_full_price(user_in_cart: Flow) -> None:
    full_price = user_in_cart.cart_page.get_full_price()
    assert full_price == Decimal('39.98'), f"Expected: 39.98. Got: {full_price}"

    
@pytest.mark.regression
def test_remove_item(user_in_cart: Flow) -> None:
    user_in_cart.cart_page.remove_item('Backpack')
    full_price = user_in_cart.cart_page.get_full_price()
    assert full_price == Decimal('9.99')
    
     
@pytest.mark.regression   
def test_remove_all_items(user_in_cart: Flow) -> None:
    user_in_cart.cart_page.remove_all()
    expect(user_in_cart.cart_page.cart_item).not_to_be_visible()
    
     
@pytest.mark.regression   
def test_continue_button(user_in_cart: Flow) -> None:
    user_in_cart.cart_page.go_to_continue_shopping()
    expect(user_in_cart.page).to_have_url(Routes.INVENTORY_URL)
    
     
@pytest.mark.smoke   
def test_checkout_button(user_in_cart: Flow) -> None:
    user_in_cart.cart_page.go_to_checkout()
    expect(user_in_cart.page).to_have_url(Routes.CHECKOUT_URL)
    



    