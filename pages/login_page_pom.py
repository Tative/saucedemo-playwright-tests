from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")
        
    def goto(self):
        self.page.goto("/")
        
    def login(self, username: str, password: str) -> None:
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        
    
        
        