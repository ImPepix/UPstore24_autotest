import random
from selenium.webdriver.common.by import By
import time

class RandomSelector:
    def __init__(self, main_page, product_page):
        self.main_page = main_page
        self.product_page = product_page

    # Метод для выбора случайной категории
    def choose_random_category(self):
        categories = self.main_page.get_categories()  # Получаем категории
        if categories:
            random_category = random.choice(categories)
            print(f"Выбрана случайная категория: {random_category.text}")
            self.main_page.scroll_to_element(random_category)  # Скролл до категории
            random_category.click()
            time.sleep(3)  # Ждем, пока категория откроется
            return True
        else:
            print("Категории не найдены.")
            return False

    # Метод для выбора случайной подкатегории
    def choose_random_subcategory(self):
        subcategories = self.main_page.get_subcategories()  # Получаем подкатегории
        if subcategories:
            random_subcategory = random.choice(subcategories)
            print(f"Выбрана случайная подкатегория: {random_subcategory.text}")
            self.main_page.scroll_to_element(random_subcategory)  # Скролл до подкатегории
            random_subcategory.click()
            time.sleep(3)  # Ждем загрузки страницы с товарами
            return True
        else:
            print("Подкатегории не найдены.")
            return False

    # Метод для выбора случайного товара
    def choose_random_product(self):
        products = self.main_page.get_products()  # Получаем список товаров
        if products:
            random_index = random.randint(0, len(products) - 1)  # Случайный индекс
            product_element = products[random_index]
            product_link = product_element.find_element(By.XPATH, ".//form[contains(@class, 'product_card-form')]//a")
            product_title = product_link.text
            print(f"Выбран случайный товар: {product_title}")
            self.main_page.scroll_to_element(product_element)  # Скролл до товара
            product_link.click()  # Переходим к товару

            # Возвращаем элемент товара и его название
            return product_element, product_title
        else:
            print("Товары не найдены.")
            return False

    # Метод для проверки, пустая ли категория (есть сообщение об этом)
    def check_if_empty_category(self):
        if self.main_page.is_empty_category_alert_visible():
            alert_message = self.main_page.get_empty_category_alert_text()
            print(f"Сообщение о пустой категории: {alert_message}")
            return True
        return False

    # Метод для проверки наличия товаров или сообщения о пустой категории
    def handle_empty_category(self):
        if self.check_if_empty_category():
            print("Категория пуста, выбираем другую категорию.")
            return False  # Пустая категория
        else:
            return True  # Есть товары
