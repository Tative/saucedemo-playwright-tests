import pytest
from playwright.sync_api import Page, expect
from logic.flow import Flow
from decimal import Decimal
from logic.routes import Routes


@pytest.fixture
def user_in_checkout(page: Page) -> Flow:
    flow = Flow(page)
    flow.authenticate()
    flow.add_items_and_go_to_cart()
    flow.go_to_checkout()
    return flow


@pytest.mark.regression
@pytest.mark.parametrize("first_name, last_name, zip_postal, error", [
    ('', 'Snow', '12345', 'Error: First Name is required'),
    ('Jhon', '', '12345', 'Error: Last Name is required'),
    ('Jhon', 'Snow', '', 'Error: Postal Code is required')
])
def test_invalid_info(user_in_checkout: Flow, first_name: str,
                      last_name: str, zip_postal: str, error: str) -> None:
    user_in_checkout.checkout_page.input_info(first_name, last_name, zip_postal)
    user_in_checkout.checkout_page.go_to_continue()
    expect(user_in_checkout.checkout_page.error).to_have_text(error)
    
    
@pytest.mark.smoke   
def test_cancel_button(user_in_checkout: Flow) -> None:
    user_in_checkout.checkout_page.go_to_cancel()
    expect(user_in_checkout.page).to_have_url(Routes.CART_URL)


@pytest.mark.smoke
def test_valid_info(user_in_checkout: Flow) -> None:
    user_in_checkout.checkout_page.input_info('Jhon', 'Snow', '12345')
    user_in_checkout.checkout_page.go_to_continue()
    expect(user_in_checkout.page).to_have_url(Routes.CHECKOUT_OVERVIEW_URL)