from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Get link
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Waiting for good price (12 sec)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    # Click "Book" button
    button = browser.find_element_by_id("book")
    button.click()

    # Execute calculations
    element = browser.find_element_by_id("input_value")
    x = element.text
    y = calc(x)

    # Put result into answer
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Submit test
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
