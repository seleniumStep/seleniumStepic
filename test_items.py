# Задание: запуск автотестов для разных языков интерфейса
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# Проверка наличия кнопки добавления в корзину
def test_check_button_basket(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element_by_class_name("btn-add-to-basket"), "Button is not available"
