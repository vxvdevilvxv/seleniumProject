import time

from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser.get(link)

    x = browser.find_element_by_tag_name('img').get_attribute('valuex')

    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
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