import pyperclip
from selenium import webdriver
import os.path

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)

    # находим и собираем элементы для заполнения
    elements = browser.find_elements_by_class_name('form-control')

    # заполняем поля любым текстом
    for element in elements:
        element.send_keys('some_text')

    # находим кнопку прикрепления файла и пеедаем в нее путь
    upload_button = browser.find_element_by_id('file')
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../file.txt')
    upload_button.send_keys(file_path)

    # находим и нажимаем кнопку отправки
    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()

    # переключаеся на алерт и считываем текст, разбиваем по пробелу и отправляем в буфер обмена число
    alert = browser.switch_to.alert
    pyperclip.copy(alert.text.split()[-1])
    alert.accept()

finally:

    browser.quit()
