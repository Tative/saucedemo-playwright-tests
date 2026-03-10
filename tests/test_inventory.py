import pytest
from playwright.sync_api import Page, expect
from logic.flow import Flow
from logic.routes import Routes

@pytest.fixture
def auth_flow(page: Page) -> Flow:
    flow = Flow(page)
    flow.authenticate()
    return flow

    
@pytest.mark.regression
def test_add_two_items_shows_cart_badge(auth_flow: Flow) -> None:
    auth_flow.inventory_page.add_items()
    expect(auth_flow.inventory_page.cart_badge).to_have_text("2")

    
@pytest.mark.smoke
def test_add_items_and_go_to_cart(auth_flow: Flow) -> None:
    auth_flow.add_items_and_go_to_cart()
    expect(auth_flow.page).to_have_url(Routes.CART_URL)
    expect(auth_flow.inventory_page.cart_items).to_have_count(2)

    
@pytest.mark.regression
def test_remove_one_item_updates_cart_badge(auth_flow: Flow) -> None:
    auth_flow.inventory_page.add_items()
    auth_flow.inventory_page.remove_backpack_from_cart()
    expect(auth_flow.inventory_page.cart_badge).to_have_text("1")
