from frontend.helpers.basepage import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class='button button--primary button--block button--medium']")  # Локатор кнопки добавления в корзину
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@class='fancybox-close-small']")  # Кнопка закрытия модального окна
    PRODUCT_TITLE = (By.XPATH, "//h1[@class='product-title']")  # Локатор заголовка товара
    CART_BUTTON = (By.XPATH, "//li[@class='user_icons-item js-user_icons-item']//a[contains(@class, 'user_icons-icon js-user_icons-icon-cart')]")  # Локатор кнопки "Открыть корзину"

    # Метод для добавления товара в корзину
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    # Метод для закрытия модального окна
    def close_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)

    # Получение названия товара
    def get_product_title(self):
        return self.get_text(self.PRODUCT_TITLE)

    # Проверка видимости модального окна
    def is_modal_visible(self):
        return self.is_visible(self.MODAL_CLOSE_BUTTON)

    # Закрытие модалки если она отобразилсь
    def check_and_close_modal(self):
        if self.is_modal_visible():
            self.close_modal()

    # Метод для перехода в корзину
    def go_to_cart(self):
        self.click(self.CART_BUTTON)
