# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage(object):
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.timeout = 30
        self.implicit_wait = 15

    def wait_till_specific_element_is_not_displayed(self, element):
        try:
            wait = WebDriverWait(self.browser, self.implicit_wait)
            expected_element = EC.visibility_of_element_located(element)
            wait.until(expected_element)
            return True
        except TimeoutError:
            raise

    def click_on_element(self, element):
        self.browser.find_element(*self.local_directories[element]).click()

    def get_text_from_element(self, element):
        try:
            a = self.browser.find_element(*self.local_directories[element])
            time.sleep(1)
        except KeyError:
            print("Element {} does not exist".format(element))
        text = a.text
        return text

    def get_attr_value(self, element):
        try:
            a = self.browser.find_element(*self.local_directories[element])
            time.sleep(1)
        except KeyError:
            print("Element {} does not exist".format(element))
        text = a.get_attribute('value')
        return text

    def get_attr_title(self, element):
        try:
            a = self.browser.find_element(*self.local_directories[element])
            time.sleep(1)
        except KeyError:
            print("Element {} does not exist".format(element))
        text = a.get_attribute('title')
        return text

    def is_element_exists(self, element):
        try:
            self.browser.find_element(*self.local_directories[element])
            time.sleep(1)
            return 1
        except KeyError:
            print("Element {} does not exist".format(element))
        return 0


