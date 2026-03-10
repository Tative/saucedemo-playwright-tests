import pytest
from playwright.sync_api import Page, expect
from logic.flow import Flow
from logic.routes import Routes


@pytest.fixture
def user_on_finish(page: Page) -> Flow:
    flow = Flow(page)
    flow.authenticate()
    flow.add_items_and_go_to_cart()
    flow.go_to_checkout()
    flow.go_to_checkout_overview()
    flow.go_to_finish_page()
    return flow


@pytest.mark.smoke
def test_back_to_broducts_button(user_on_finish: Flow) -> None:
    user_on_finish.finish_page.go_to_back_to_products()
    expect(user_on_finish.page).to_have_url(Routes.INVENTORY_URL)
    
   
@pytest.mark.smoke 
def test_finish_header(user_on_finish: Flow) -> None:
    expect(user_on_finish.finish_page.finish_header).to_have_text(user_on_finish.finish_page.get_finish_text())