from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Get the 1st number
    element = browser.find_element_by_id("num1")
    num1 = int(element.text)

    # Get the 2n number
    element = browser.find_element_by_id("num2")
    num2 = int(element.text)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(num1 + num2))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()