from playwright.sync_api import Page, Locator
from decimal import Decimal
import allure


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_field = page.get_by_placeholder("First Name")
        self.last_name_field = page.get_by_placeholder("Last Name")
        self.zip_postal_field = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role('button', name='Continue')
        self.cancel_button = page.get_by_role('button', name='Cancel')
        self.error = page.get_by_test_id('error')
        
    
    @allure.step("Ввод информации о покупателе")
    def input_info(self, first_name: str, last_name: str, zip_postal: str) -> None:
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.zip_postal_field.fill(zip_postal)
    
    
    @allure.step("Переход к странице оформления заказа")
    def go_to_continue(self) -> None:
        self.continue_button.click()
        
        
    @allure.step("Переход к корзине при отмене оформления заказа")
    def go_to_cancel(self) -> None:
        self.cancel_button.click()
        
        
    def get_error_field(self) -> Locator:
        return self.error
    
