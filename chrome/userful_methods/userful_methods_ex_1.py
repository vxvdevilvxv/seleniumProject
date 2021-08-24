from selenium import webdriver
import math


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/math.html'

try:
    browser.get(link)

    # ищем элемент с необходимым значением на странице
    x = browser.find_element_by_id('input_value').text

    # вставляем в форму ответа результат расчета по формуле
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    # находим отмечаем чек-бокс
    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()

    # находим отмечаем радио-кнопку
    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobutton.click()

    # находим и нажимаем кнопку отправки
    submit = browser.find_element_by_class_name('btn-default')
    submit.click()

    # переключаеся на алерт и считываем текст, разбиваем по пробелу и вытаскиваем необходимое число
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


except Exception as ex:
    print(ex)

finally:
    browser.quit()
