from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchBar(BasePage):

    local_directories = {
        "searching_bar": (
            By.ID, 'horus-querytext'),
        "searching_button": (
            By.CLASS_NAME, 'horus-btn-search'),


    }

    def insert_text_to_search_bar(self, text):
        self.browser.find_element(*self.local_directories["searching_bar"]).send_keys(text)