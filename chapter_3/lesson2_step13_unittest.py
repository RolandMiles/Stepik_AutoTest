from selenium import webdriver
import unittest
import time


class TestUnit(unittest.TestCase):

    def test_page_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # First name
        element = browser.find_element_by_css_selector(".first_block .first")
        element.send_keys(".first_block .first")

        # Last name
        element = browser.find_element_by_css_selector(".first_block .second")
        element.send_keys(".first_block .second")

        # Email
        element = browser.find_element_by_css_selector(".first_block .third")
        element.send_keys(".first_block .third")

        # Phone
        element = browser.find_element_by_css_selector(".second_block .first")
        element.send_keys(".second_block .first")

        # Address
        element = browser.find_element_by_css_selector(".second_block .second")
        element.send_keys(".second_block .second")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text is incorrect")

        # Ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_page_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # First name
        element = browser.find_element_by_css_selector(".first_block .first")
        element.send_keys(".first_block .first")

        # Last name
        element = browser.find_element_by_css_selector(".first_block .second")
        element.send_keys(".first_block .second")

        # Email
        element = browser.find_element_by_css_selector(".first_block .third")
        element.send_keys(".first_block .third")

        # Phone
        element = browser.find_element_by_css_selector(".second_block .first")
        element.send_keys(".second_block .first")

        # Address
        element = browser.find_element_by_css_selector(".second_block .second")
        element.send_keys(".second_block .second")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text is incorrect")

        # Ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()