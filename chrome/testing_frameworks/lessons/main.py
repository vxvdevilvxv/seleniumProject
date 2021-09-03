from selenium import webdriver
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        # тут, как и предполагалось авторами курса, проверяем по суперуникальному селектору наличие трех обязательных полей first_name, last_name, email
        first_name = browser.find_element_by_css_selector('div.first_block input.form-control.first:required')
        first_name.send_keys('some_text')
        last_name = browser.find_element_by_css_selector('div.first_block input.form-control.second:required')
        last_name.send_keys('some_text')
        email = browser.find_element_by_css_selector('div.first_block input.form-control.third:required')
        email.send_keys('some_text')

        # достаем кнопку, она одна единственная на странице, поэтому пользуемся тегом
        button = browser.find_element_by_tag_name("button")
        button.click()

        self.assertEqual(browser.find_element_by_tag_name("h1").text,
                         'Congratulations! You have successfully registered!',
                         "Should be Congratulations! You have successfully registered!")

    def test_abs2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        # тут, как и предполагалось авторами курса, проверяем по суперуникальному селектору наличие трех обязательных полей first_name, last_name, email
        first_name = browser.find_element_by_css_selector('div.first_block input.form-control.first:required')
        first_name.send_keys('some_text')
        last_name = browser.find_element_by_css_selector('div.first_block input.form-control.second:required')
        last_name.send_keys('some_text')
        email = browser.find_element_by_css_selector('div.first_block input.form-control.third:required')
        email.send_keys('some_text')

        # достаем кнопку, она одна единственная на странице, поэтому пользуемся тегом
        button = browser.find_element_by_tag_name("button")
        button.click()

        self.assertEqual('Congratulations! You have successfully registered!',
                         browser.find_element_by_tag_name("h1").text,
                         "Should be Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
