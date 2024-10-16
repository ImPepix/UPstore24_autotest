from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Метод для открытия URL
    def open(self, url):
        self.driver.get(url)

    # Поиск одного элемента
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # Поиск нескольких элементов
    def finds(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    # Клик по элементу с ожиданием кликабельности
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        element.click()

    def go_back(self):
        self.driver.back()

    # Ввод текста в элемент
    def input_text(self, locator, text):
        element = self.find(locator)
        element.clear()  # Очистка перед вводом
        element.send_keys(text)

    # Проверка видимости элемента на странице
    def is_visible(self, locator):
        try:
            element = self.find(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    # Получение текста элемента
    def get_text(self, locator):
        element = self.find(locator)
        return element.text

    # Ожидание, пока элемент станет видимым
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # Скролл до элемента
    def scroll_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()  # Прокрутка до элемента