import pytest
from playwright.sync_api import Page, expect
from logic.flow import Flow
from decimal import Decimal
from logic.routes import Routes


@pytest.fixture
def user_in_overview(page: Page) -> Flow:
    flow = Flow(page)
    flow.authenticate()
    flow.add_items_and_go_to_cart()
    flow.go_to_checkout()
    flow.go_to_checkout_overview()
    return flow

    
@pytest.mark.smoke 
def test_cancel_button(user_in_overview: Flow) -> None:
    user_in_overview.checkout_overview_page.go_to_cancel()
    expect(user_in_overview.page).to_have_url(Routes.INVENTORY_URL)

    
@pytest.mark.smoke 
def test_finish_button(user_in_overview: Flow) -> None:
    user_in_overview.checkout_overview_page.go_to_finish()
    expect(user_in_overview.page).to_have_url(Routes.FINISH_URL)

    
@pytest.mark.smoke 
def test_tax_price(user_in_overview: Flow) -> None:
    expected_tax = user_in_overview.checkout_overview_page.get_tax_price()
    expect(user_in_overview.checkout_overview_page.tax_price).to_contain_text(str(expected_tax))

    
@pytest.mark.smoke 
def test_subtotal_price(user_in_overview: Flow) -> None:
    subtotal_expected = user_in_overview.checkout_overview_page.get_subtotal_price()
    expect(user_in_overview.checkout_overview_page.subtotal_price).to_contain_text(str(subtotal_expected))

    
@pytest.mark.smoke 
def test_total_price(user_in_overview: Flow) -> None:
    total_expected = user_in_overview.checkout_overview_page.get_total_price()
    expect(user_in_overview.checkout_overview_page.total_price).to_contain_text(str(total_expected))
    print(f"/////////////////////{total_expected}////////////////////////")
 
    
@pytest.mark.regression 
def test_items_in_cart(user_in_overview: Flow) -> None:
    print(f"DEBUG Items in cart: {user_in_overview.checkout_overview_page.cart_item.count()}")
    expect(user_in_overview.checkout_overview_page.cart_item).to_have_count(2)
    
    
    