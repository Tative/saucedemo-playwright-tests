from playwright.sync_api import Page
import allure


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_backpack_button = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.add_bike_button = page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.remove_backpack = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        self.cart_button = page.locator("[data-test=\"shopping-cart-link\"]")
        self.remove_bike = page.locator("[data-test=\"remove-sauce-labs-bike-light\"]")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_items = page.locator(".cart_item")


    @allure.step("Добавление рюкзака в корзину")
    def add_backpack(self):
        self.add_backpack_button.click()


    @allure.step("Добавление велосипеда в корзину")
    def add_bike(self):
        self.add_bike_button.click()
        
        
    @allure.step("Добавление рюкзака и велосипеда в корзину") 
    def add_items(self):
        self.add_backpack()
        self.add_bike()
        
    
    @allure.step("Удаление рюкзака из корзины")    
    def remove_backpack_from_cart(self):
        self.remove_backpack.click() 
        
     
    @allure.step("Удаление велосипеда из корзины")
    def remove_bike_from_cart(self):
        self.remove_bike.click()
        
        
    @allure.step("Переход в корзину")
    def go_to_cart(self):
        self.cart_button.click()
    
        
        
