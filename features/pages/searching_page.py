from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchingPage(BasePage):

    local_directories = {
        "searching_filter": (
            By.ID, 'js_filterlist'),
        "option_wife": (
            By.CSS_SELECTOR, "button[title='Free WiFi'] .fl-group__btn"),
        "option_spa": (
            By.CSS_SELECTOR, "button[title='Spa'] .fl-group__btn"),
        "searching_area": (By.CLASS_NAME, 'name__copytext')


    }

