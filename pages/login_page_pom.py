from playwright.sync_api import Page
import allure


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")
        
        
    @allure.step("Переход на страницу логина")
    def goto(self) -> None:
        self.page.goto("/")
        
        
    @allure.step("Ввод логина и пароля и нажатие кнопки входа") 
    def login(self, username: str, password: str) -> None:
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        
    
        
        