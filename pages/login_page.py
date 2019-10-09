from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка корректности URL
    def should_be_login_url(self):
        print(self.url)
        assert self.browser.current_url, 'Login link is not found'

    # Проверка наличия на странице формы логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_SELECTOR), 'Login form not found'

    # Проверка наличия на странице формы регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SELECTOR), 'Registration form not found'

    # Регистрация нового пользователя
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS_CONF).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

