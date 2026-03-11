from playwright.sync_api import Page, Locator
import allure

class FinishPage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_header = page.get_by_test_id("complete-header")
        self.back_to_products_button = page.get_by_role('button', name='Back Home')
        
    
    @allure.step("Получение текста о завершении заказа")
    def get_finish_text(self) -> str:
        finish_text = "Thank you for your order!"
        return finish_text
    
    
    @allure.step("Переход к странице инвенторя при нажатии кнопки 'Back Home")
    def go_to_back_to_products(self) -> None:
        self.back_to_products_button.click() 