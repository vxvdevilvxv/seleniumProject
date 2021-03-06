import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

try:
    browser.get(link)

    # ищем элементы с необходимым значением на странице
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text

    # находим поле селект и преобразуем его в объект класса с последующим выбором ответа
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(int(num1) + int(num2)))

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
