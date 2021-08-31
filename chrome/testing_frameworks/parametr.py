import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1'
         ]

message = ''


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

    print()
    print("=====================")
    print(message)


class TestParam:

    @pytest.mark.parametrize('link', links)
    def test_ufo(self, browser, link):
        global message

        browser.get(link)
        browser.implicitly_wait(5)
        text_form = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area")))
        text_form.send_keys(str(math.log(int(time.time()))))
        button = browser.find_element_by_css_selector('button.submit-submission')
        button.click()
        text = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'pre.smart-hints__hint'))).text
        if 'Correct!' not in text:
            message += text

        assert "Correct!" in text
