from selenium import webdriver
import time

def test(link):
    browser = webdriver.Chrome()

    try:
        browser.get(link)

        #тут, как и предполагалось авторами курса, проверяем по суперуникальному селектору наличие трех обязательных полей first_name, last_name, email
        first_name = browser.find_element_by_css_selector('div.first_block input.form-control.first:required')
        first_name.send_keys('some_text')
        last_name = browser.find_element_by_css_selector('div.first_block input.form-control.second:required')
        last_name.send_keys('some_text')
        email = browser.find_element_by_css_selector('div.first_block input.form-control.third:required')
        email.send_keys('some_text')

        #достаем кнопку, она одна единственная на странице, поэтому пользуемся тегом
        button = browser.find_element_by_tag_name("button")
        button.click()

        # ждем 5 секунд, чтоб скопировать код
        time.sleep(5)

        #тут достаем текст в случае успешного перехода
        welcome_text = browser.find_element_by_tag_name("h1").text

        #возвращаем текст
        return welcome_text

    finally:

        # закрываем браузер после всех манипуляций
        browser.quit()

assert "Congratulations! You have successfully registered!" == test("http://suninjuly.github.io/registration1.html")
assert "Congratulations! You have successfully registered!" == test("http://suninjuly.github.io/registration2.html")
