from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Проверяем что корзина пуста
    def basket_not_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), 'Basket is not empty'

    # Проверяем что есть сообщение о пустой корзине
    def empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), 'Not text of empty basket'

