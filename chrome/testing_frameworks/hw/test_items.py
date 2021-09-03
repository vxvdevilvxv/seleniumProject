import time
import unittest

class TestPage:
    def test_language_option(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        # 30 секунд (если лень ждать столько, поставь меньше) для проверки французского языка,
        # просто раскомментируй сроку ниже ↓ и не благодари за заботу)
        #time.sleep(30)
        button = len(browser.find_elements_by_css_selector('#add_to_basket_form button.btn-add-to-basket'))
        assert button > 0, 'Button is not found'

if __name__ == '__main__':
    unittest.main()