from playwright.sync_api import Page

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

    def add_backpack(self):
        self.add_backpack_button.click()

    def add_bike(self):
        self.add_bike_button.click()
        
    def add_items(self):
        self.add_backpack()
        self.add_bike()
        
    def remove_backpack_from_cart(self):
        self.remove_backpack.click() 
        
    def remove_bike_from_cart(self):
        self.remove_bike.click()
        
    def go_to_cart(self):
        self.cart_button.click()
    
        
        
