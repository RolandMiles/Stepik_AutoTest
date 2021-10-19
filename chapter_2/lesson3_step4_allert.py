from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Get button element on page
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
    btn = browser.find_element_by_class_name("btn")
    btn.click()

    # Switch to alert and confirm it
    confirm = browser.switch_to.alert
    confirm.accept()

    # Execute calculations
    element = browser.find_element_by_id("input_value")
    x = element.text
    y = calc(x)

    # Put result into answer
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Submit test
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
