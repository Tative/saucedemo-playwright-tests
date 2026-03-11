import allure
from playwright.sync_api import Page
from config import Config
from pages.login_page_pom import LoginPage
from pages.inventory_page_pom import InventoryPage
from pages.cart_page_pom import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.finish_page_pom import FinishPage


class Flow:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.cart_page = CartPage(page)
        self.checkout_page = CheckoutPage(page)
        self.checkout_overview_page = CheckoutOverviewPage(page)
        self.finish_page = FinishPage(page)
        
        
    @allure.step("Аутентификация пользователя с именем: {username}")
    def authenticate(self, username: str = Config.USER_NAME, password: str = Config.PASSWORD) -> None:
        self.login_page.goto()
        self.login_page.login(username, password)
        

    @allure.step("Добавление товаров в корзину и переход на страницу корзины")    
    def add_items_and_go_to_cart(self) -> None:
        self.inventory_page.add_bike()
        self.inventory_page.add_backpack()
        self.inventory_page.go_to_cart()
        

    @allure.step("Переход на страницу оформления заказа")
    def go_to_checkout(self) -> None:
        self.cart_page.go_to_checkout()
        
        
    @allure.step("Переход на страницу обзора заказа")
    def go_to_checkout_overview(self) -> None:
        self.checkout_page.input_info(Config.FIRST_NAME, Config.LAST_NAME, Config.POSTAL_CODE)
        self.checkout_page.go_to_continue()
        
        
    @allure.step("Переход на финальную страницу")
    def go_to_finish_page(self) -> None:
        self.checkout_overview_page.go_to_finish()
        
        