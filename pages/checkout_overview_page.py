from playwright.sync_api import Page
from decimal import Decimal
import allure


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.subtotal_price = page.get_by_test_id('subtotal-label')
        self.tax_price = page.get_by_test_id('tax-label')
        self.total_price = page.get_by_test_id('total-label')
        self.cancel_button = page.get_by_test_id('cancel')
        self.finish_button = page.get_by_test_id('finish')
        self.cart_item = page.get_by_test_id('inventory-item')
        
        
    @allure.step("Переход к странице инвентаря при отмене заказа из чекаута")
    def go_to_cancel(self) -> None:
        self.cancel_button.click()
        
    
    @allure.step("Переход к странице завершения заказа")
    def go_to_finish(self) -> None:
        self.finish_button.click()
        
    
    @allure.step("Получение количества товаров в корзине")
    def get_count_items_in_cart(self) -> int:
        count = self.cart_item.count()
        return count
        
        
    @allure.step("Получение общей стоимости товаров без налога")
    def get_subtotal_price(self) -> Decimal:
        price_items: list[str] = self.cart_item.get_by_test_id('inventory-item-price').all_inner_texts()
        subtotal_price_sum = sum(Decimal(p.replace('$', '').strip()) for p in price_items)
        return subtotal_price_sum
        
        
    @allure.step("Расчет суммы налога (8%)")
    def get_tax_price(self) -> Decimal:
        subtotal_sum = self.get_subtotal_price()
        tax_raw: Decimal = subtotal_sum * Decimal('0.08')
        tax = tax_raw.quantize(Decimal('0.01'))
        return tax
        
        
    @allure.step("Получение общей стоимости товаров с налогом")
    def get_total_price(self) -> Decimal:
        subtotal_sum = self.get_subtotal_price()
        tax = self.get_tax_price()
        total_price = subtotal_sum + tax
        return total_price
        