import time

import pyperclip
from selenium import webdriver
import math, os.path


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get(link)

    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()

    confirm = browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id('input_value').text

    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()

    alert = browser.switch_to.alert
    pyperclip.copy(alert.text.split()[-1])
    alert.accept()

except Exception as ex:
    print(ex)

finally:
    browser.quit()
