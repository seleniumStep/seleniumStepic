from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    REGISTRATION_SELECTOR = (By.CSS_SELECTOR, '#register_form')
    LOGIN_SELECTOR = (By.CSS_SELECTOR, '#login_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS_CONF = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME_TO_BASKET = (By.CSS_SELECTOR, '#messages div.alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    TITLE_PAGE_PRODUCT = (By.CSS_SELECTOR, '')
    SUCCESS_MESSAGE_BASKET = (By.CSS_SELECTOR, '#messages div div')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')

