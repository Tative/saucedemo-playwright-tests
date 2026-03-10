from playwright.sync_api import Page
from decimal import Decimal

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item = page.get_by_test_id('inventory-item')
        self.remove_button = page.get_by_role('button', name='Remove')
        self.continue_shopping_button = page.get_by_test_id('continue-shopping')
        self.checkout_button = page.get_by_test_id('checkout')
        
        
    def remove_item(self, name: str) -> None:
        self.cart_item.filter(has_text=name).get_by_role('button', name='Remove').click()
        
    def remove_all(self) -> None:
        buttons = self.page.get_by_role('button', name='Remove')
        while buttons.count() > 0:
            buttons.first.click()
        
    def get_full_price(self) -> Decimal:
        prices_list = self.page.get_by_test_id('inventory-item-price').all_inner_texts()
        full_price = sum(Decimal(p.replace('$', '').strip()) for p in prices_list)
        return full_price
    
    def go_to_continue_shopping(self) -> None:
        self.continue_shopping_button.click()
        
    def go_to_checkout(self) -> None:
        self.checkout_button.click()
        
    
    
    