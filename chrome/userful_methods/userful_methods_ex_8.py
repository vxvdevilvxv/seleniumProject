import math
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()

try:

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет приемлемой
    price = WebDriverWait(browser, 12).until(
        text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    # находим и нажимаем кнопку
    button = browser.find_element_by_id('book')
    button.click()

    # ищем элемент с необходимым значением на странице
    x = browser.find_element_by_id('input_value').text

    # вставляем в форму ответа результат расчета по формуле
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    # находим и нажимаем кнопку отправки
    submit = browser.find_element_by_id('solve')
    submit.click()

    # переключаеся на алерт и считываем текст, разбиваем по пробелу и отправляем в буфер обмена число
    alert = browser.switch_to.alert
    pyperclip.copy(alert.text.split()[-1])
    alert.accept()

except Exception as ex:
    print(ex)

finally:

    browser.quit()
