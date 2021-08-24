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

    # находим и нажимаем кнопку
    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()

    # переключаемся между вкладками
    browser.switch_to.window(browser.window_handles[1])

    # ищем элемент с необходимым значением на странице
    x = browser.find_element_by_id('input_value').text

    # вставляем в форму ответа результат расчета по формуле
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    # находим и нажимаем кнопку отправки
    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()

    # переключаеся на алерт и считываем текст, разбиваем по пробелу и отправляем в буфер обмена число
    alert = browser.switch_to.alert
    pyperclip.copy(alert.text.split()[-1])
    alert.accept()

except Exception as ex:
    print(ex)

finally:
    browser.quit()
