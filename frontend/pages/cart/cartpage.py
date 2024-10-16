from frontend.helpers.basepage import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    CART_PAGE_HEADER = (By.XPATH, "//h1[contains(text(), 'Корзина')]")
    CART_PRODUCT_TITLE = (By.XPATH, "//div[@class='cart-items']//div[contains(@class, 'cart-item-title')]/a")
    CHECKOUT_BUTTON = (By.XPATH, "//input[@type='submit']")
    ORDER_ITEM_TITLE = (By.XPATH, "//div[@class='co-basket_item-description']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//*[@id='create_order']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'co-notice--success')]")

    # Ожидание загрузки страницы корзины
    def wait_for_cart_page(self):
        self.wait_for_element(self.CART_PAGE_HEADER)

    # Получение названия товара в корзине
    def get_product_title(self):
        return self.get_text(self.CART_PRODUCT_TITLE)

    # Нажатие на кнопку 'Оформить заказ'
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    # Нажатие на кнопку 'Подтвердить заказ'
    def confirm_order(self):
        self.click(self.CONFIRM_ORDER_BUTTON)

    # Ожидание и проверка названия товара на странице оформления заказа
    def verify_order_item_title(self, expected_title):
        self.wait_for_element(self.ORDER_ITEM_TITLE)
        actual_title = self.get_text(self.ORDER_ITEM_TITLE)
        assert actual_title == expected_title, f"Ожидалось название товара '{expected_title}', но было '{actual_title}'"

    # Метод для проверки наличия сообщения об успешном заказе
    def is_order_success_message_visible(self):
        return self.is_visible(self.SUCCESS_MESSAGE)

    # Метод для получения текста сообщения об успешном заказе
    def get_order_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

