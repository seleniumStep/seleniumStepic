import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

default_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
    pytest.param(
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
        marks=pytest.mark.xfail
    ),
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_title_and_product_name()
    page.check_adding_product_to_basket()
    page.basket_and_product_price()


# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, default_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


# Открываем страницу товара
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, default_link)
    page.open()
    page.should_not_be_success_message()


# Открываем страницу товара
# Добавляем товар в корзину
# Проверяем, что нет сообщения об успехе с помощью is_disappeared
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, default_link)
    page.open()
    page.add_product_to_basket()
    time.sleep(1)
    page.success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


# Гость открывает страницу товара
# Переходит в корзину по кнопке в шапке
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, default_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_not_products()
    basket_page.empty_basket_text()


class TestUserAddToBasketFromProductPage:
    # Открываем страницу регистрации
    # Регистрируем нового пользователя
    # Проверяем, что пользователь залогинен
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        email = 'testEmail' + str(time.time()) + '@test.ru'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, '123Password!!!')
        page.should_be_authorized_user()

    # Открываем страницу товара
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, default_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, default_link)
        page.open()
        page.add_product_to_basket()
        page.check_title_and_product_name()
        page.check_adding_product_to_basket()
        page.basket_and_product_price()