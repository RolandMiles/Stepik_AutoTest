from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    element = browser.find_element_by_id("treasure")
    x = element.get_attribute("valuex")

    y = calc(x)

    element = browser.find_element_by_id("answer")
    element.send_keys(y)

    element = browser.find_element_by_id("robotCheckbox")
    element.click()

    element = browser.find_element_by_id("robotsRule")
    element.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
