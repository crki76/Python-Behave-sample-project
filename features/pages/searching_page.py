from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class SearchingPage(BasePage):

    local_directories = {
        "searching_filter": (
            By.ID, 'js_filterlist'),
        "option_wife": (
            By.CLASS_NAME, 'fl-group__btn--top-wifi'),
        "option_spa": (
            By.CLASS_NAME, 'fl-group__btn--top-wellness'),
        "wife_selected": (By.CSS_SELECTOR, "button[title='Free WiFi'] .fl-group__btn"),
        "spa_selected": (By.CSS_SELECTOR, "button[title='Spa'] .fl-group__btn"),
        "item_details": (By.CLASS_NAME, 'item__details')

    }

