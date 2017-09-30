from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchBar(BasePage):

    local_directories = {
        "searching_bar": (
            By.ID, 'horus-querytext'),
        "searching_button": (
            By.CLASS_NAME, 'horus-btn-search')

    }