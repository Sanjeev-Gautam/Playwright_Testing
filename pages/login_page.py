from playwright.sync_api import Page 
from config import BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('input[name="user-name"]')
        self.password = page.locator('input[name="password"]')
        self.login_button = page.locator('input[type="submit"]')

    def navigate(self):
        print(f"Base URL: {BASE_URL}")  # Debugging line to check the value of BASE_URL
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

        