from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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