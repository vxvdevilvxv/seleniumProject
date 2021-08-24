from selenium import webdriver
import time, os.path

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)

    elements = browser.find_elements_by_class_name('form-control')

    for element in elements:
        element.send_keys('some_text')

    upload_button = browser.find_element_by_id('file')
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')
    upload_button.send_keys(file_path)

    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:

    browser.quit()
