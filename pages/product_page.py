from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Добавление товара в корзину
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    # Проверка добаления товара в корзину
    def check_adding_product_to_basket(self):
        check = self.is_element_present(*ProductPageLocators.PRODUCT_NAME_TO_BASKET)
        print('\n--> Product added to basket') if check else print('\n--> Product NOT added to basket')
        assert check, 'Selector not found'

    # Проверка стоимости корзины со стоимостью товара
    def basket_and_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        print('\n--> Basket ' + basket_price)
        print('\n--> Basket price == product price ', product_price == basket_price)
        assert product_price == basket_price, 'Product price is not equal basket price'

    # Получение название товара на странице
    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Selector not found'
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    # Получени цены товара на странице
    def get_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'Selector not found'
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    # Получение заголовка товара
    def get_title_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # Проверка совпадения название товара в сообщении с заголовком товара на странице
    def check_title_and_product_name(self):
        title = self.get_title_product()
        basket_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TO_BASKET).text
        assert basket_message.strip() == title.strip(), 'Title mismatch product name'

    # Проверка не появления блока с сообщением
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_BASKET), (
            'Success message is presented, but should not be'
        )

    # Проверка появления блока с сообщением
    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_BASKET), (
            'Add to cart successful message has not disappeared'
        )
