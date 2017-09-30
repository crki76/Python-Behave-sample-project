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