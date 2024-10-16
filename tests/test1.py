from frontend.pages.mainpage.mainpage import MainPage
from frontend.pages.product.productpage import ProductPage
from frontend.pages.cart.cartpage import CartPage
from frontend.pages.auth.authpage import AuthPage
from frontend.helpers.randomize import RandomSelector

class TestCatalog:
    def test_catalog(self, browser):
        main_page = MainPage(browser)
        product_page = ProductPage(browser)
        cart_page = CartPage(browser)
        auth_page = AuthPage(browser)
        selector = RandomSelector(main_page, product_page)

        # Шаг 1: Открываем главную страницу
        main_page.open("https://upstore24.ru")
        print("\nОткрыта главная страница.")

        # Шаг 2: Переход на страницу регистрации
        print("Переход на страницу регистрации...")
        main_page.hover_and_click_registration()
        print("Регистрация нового пользователя...")
        auth_page.fill_registration_form()
        print("Регистрация завершена.")

        # Шаг 3: Проверяем, открылась ли страница истории заказов
        main_page.wait_for_redirect_to_order_history()

        # Шаг 4: Переход в каталог
        main_page.click_catalog()

        # Шаг 5: Цикл выбора категории
        while True:
            if not selector.choose_random_category():
                print("Не удалось выбрать категорию. Завершение теста.")
                break

            # Шаг 6: Есть ли товары в выбранной категории
            if selector.check_if_empty_category():
                print("Категория пуста, выбираем другую категорию.")
                continue  # Если категория пуста — возвращаемся к выбору другой

            # Проверяем наличие подкатегорий
            if main_page.has_subcategories():
                print("Найдены подкатегории, выбираем случайную подкатегорию...")
                if not selector.choose_random_subcategory():
                    print("Не удалось выбрать подкатегорию.")
                    continue  # Если подкатегория не выбрана — возвращаемся к выбору

                # Проверяем, пуста ли подкатегория
                if selector.check_if_empty_category():
                    print("Подкатегория пуста, возвращаемся назад.")
                    main_page.go_back()  # Возвращаемся назад, если подкатегория пуста
                    continue  # Пробуем выбрать другую категорию

            # Шаг 7: Если есть товары в подкатегории или основной категории — выбираем товар
            if not selector.choose_random_product():
                print("Не удалось выбрать товар. Переход к другой категории.")
                continue

            # Шаг 8: Получаем название выбранного товара
            try:
                product_title = product_page.get_product_title()
            except Exception as e:
                print(f"Ошибка при получении названия товара: {e}")
                continue

            # Шаг 9: Добавляем товар в корзину
            product_page.add_to_cart()
            print(f"Товар '{product_title}' добавлен в корзину.")

            # Шаг 10: Закрываем модальное окно, если оно появилось
            product_page.check_and_close_modal()
            print("Модальное окно закрыто.")

            # Шаг 11: Переходим в корзину
            product_page.go_to_cart()
            cart_page.wait_for_cart_page()
            print("Переход в корзину.")

            # Шаг 12: Проверяем название товара в корзине
            cart_product_title = cart_page.get_product_title()
            assert cart_product_title == product_title, "Ошибка: Товар в корзине не совпадает с добавленным!"
            print(f"Товар '{cart_product_title}' успешно добавлен в корзину.")

            # Шаг 13: Переходим к оформлению заказа
            cart_page.click_checkout()

            # Шаг 14: Проверяем название товара на странице оформления заказа
            cart_page.verify_order_item_title(product_title)
            print(f"Название товара на странице оформления совпадает: {product_title}")

            # Шаг 15: Подтверждаем заказ
            cart_page.confirm_order()
            print("Заказ успешно оформлен.")

            # Шаг 16: Проверяем сообщение об успешном оформлении заказа
            assert cart_page.is_order_success_message_visible(), "Ошибка: Сообщение о заказе не отображается!"
            success_message = cart_page.get_order_success_message()
            print(f"Сообщение: {success_message}")

            break