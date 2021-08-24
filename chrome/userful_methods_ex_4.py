from selenium import webdriver
import math, os.path


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser.get(link)

    x = browser.find_element_by_id('input_value').text

    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))
    browser.execute_script('button = document.getElementsByTagName("button")[0];\
                            button.scrollIntoView(true);')

    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobutton.click()

    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

except Exception as ex:
    print(ex)

finally:
    browser.quit()
