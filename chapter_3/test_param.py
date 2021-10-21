import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser...")
    browser.quit()


@pytest.mark.parametrize("link", ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_stepik(browser, link):
    answer = math.log(int(time.time()))
    browser.get(link)

    ans = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
    ans.send_keys(answer)

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    button.click()

    message = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__feedback")))

    assert message.text == "Correct!", f"Answer is {message.text}"




