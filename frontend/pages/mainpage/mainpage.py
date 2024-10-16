from frontend.helpers.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы
    ORDER_HISTORY_TITLE = (By.XPATH, "//h1[contains(text(), 'История заказов')]")
    CATALOG_BUTTON = (By.XPATH, "//ul[@class='nav-items list-unstyled js-nav-items']/li[2]/a")
    CATEGORY_LINKS = (By.XPATH, "//nav[@class='nav-sidebar js-nav-sidebar-clone']/ul/li/a")
    SUBCATEGORY_LINKS = (By.XPATH, "//div[@class='subcollections']/div/div")
    PRODUCT_LINKS = (By.XPATH, "//div[@class='products']/div/div")
    EMPTY_CATEGORY_ALERT = (By.XPATH, "//div[@class='alert alert--default']//div[@class='col']")
    PRODUCT_TITLE = (By.XPATH, "//form[@class='product_card-form']//div[@class='product_card-title']/a")
    PROFILE_BUTTON = (By.XPATH, "//li[contains(@class, 'user_icons-item') and contains(@class, 'js-user_icons-item nav-hide')]//a[contains(@class, 'user_icons-icon')]")
    REGISTRATION_BUTTON = (By.XPATH, "//div[contains(@class, 'dropdown_products-action')]//a[contains(@href, '/client_account/contacts/new')]")

    # Ождание редиректа после регистрации
    def wait_for_redirect_to_order_history(self):
        self.wait_for_element(self.ORDER_HISTORY_TITLE)

    # Нажатие на кнопку каталог
    def click_catalog(self):
        self.click(self.CATALOG_BUTTON)

    # Наведение на кнопку регистрации и клик по ней
    def hover_and_click_registration(self):
        ActionChains(self.driver).move_to_element(self.find(self.PROFILE_BUTTON)).perform()
        self.click(self.REGISTRATION_BUTTON)

    # Получение категорий
    def get_categories(self):
        return self.finds(self.CATEGORY_LINKS)

    # Проверка есть ли подкатеегории
    def has_subcategories(self):
        try:
            subcategories = self.driver.find_elements(*self.SUBCATEGORY_LINKS)
            return len(subcategories) > 0
        except Exception as e:
            print(f"Ошибка при проверке подкатегорий: {e}")
            return False

    # Получение подкатегорий
    def get_subcategories(self):
        return self.finds(self.SUBCATEGORY_LINKS)

    # Получение товаров
    def get_products(self):
        return self.finds(self.PRODUCT_LINKS)

    # Проверка видимости уведомления о пустой категории
    def is_empty_category_alert_visible(self):
        return self.is_visible(self.EMPTY_CATEGORY_ALERT)

    # Получение текста уведомления о пустой категории
    def get_empty_category_alert_text(self):
        return self.get_text(self.EMPTY_CATEGORY_ALERT)

    # Получение названия товара
    def get_product_title(self):
        product_title_element = self.find(self.PRODUCT_TITLE)
        return product_title_element.text
