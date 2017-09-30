from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchingPage(BasePage):

    local_directories = {
        "searching_filter": (
            By.ID, 'js_filterlist')

    }