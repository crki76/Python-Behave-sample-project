from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class HomePage(BasePage):

    project_url = "https://www.trivago.ie/"

    local_directories = {

        "slogan": (
            By.CLASS_NAME, 'hero__title'),
        "filter_on_search_page": (
            By.ID, 'js_filterlist')

    }