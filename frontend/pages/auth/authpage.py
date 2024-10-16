from frontend.helpers.basepage import BasePage
from selenium.webdriver.common.by import By
from faker import Faker

class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.faker = Faker('ru_RU')

    PAGE_TITLE = (By.XPATH, "//h1[contains(@class, 'co-checkout-title')]")
    FULL_NAME_CONTAINER = (By.XPATH, "//*[@id='new_client']/div[1]")
    FULL_NAME_INPUT = (By.CSS_SELECTOR, "input[id='client_contact_name']")

    PHONE_CONTAINER = (By.XPATH, "//*[@id='new_client']/div[2]")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[id='client_phone']")

    EMAIL_CONTAINER = (By.XPATH, "//*[@id='new_client']/div[3]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='client_email']")

    PASSWORD_CONTAINER = (By.XPATH, "//*[@id='new_client']/div[5]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='client_password']")

    CONFIRM_PASSWORD_CONTAINER = (By.XPATH, "//*[@id='new_client']/div[6]")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='client_password_confirmation']")

    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'co-button')]")

    def fill_registration_form(self):
        full_name = self.faker.name()
        phone = self.faker.phone_number()
        email = self.faker.email()
        password = self.faker.password()

        self.click(self.FULL_NAME_CONTAINER)
        self.input_text(self.FULL_NAME_INPUT, full_name)

        self.click(self.PHONE_CONTAINER)
        self.input_text(self.PHONE_INPUT, phone)

        self.click(self.EMAIL_CONTAINER)
        self.input_text(self.EMAIL_INPUT, email)

        self.click(self.PASSWORD_CONTAINER)
        self.input_text(self.PASSWORD_INPUT, password)

        self.click(self.CONFIRM_PASSWORD_CONTAINER)
        self.input_text(self.CONFIRM_PASSWORD_INPUT, password)

        self.click(self.REGISTER_BUTTON)