import time

from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/math.html'

try:
    browser.get(link)

    x = browser.find_element_by_id('input_value').text

    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobutton.click()

    submit = browser.find_element_by_class_name('btn-default')
    submit.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


except Exception as ex:
    print(ex)

finally:
    browser.quit()