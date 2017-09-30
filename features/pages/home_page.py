from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class HomePage(BasePage):
    project_url = "https://www.trivago.ie"

    local_directories = {
        "trivago_logo": (
            By.ID, 'svg-logo-title'),
        "slogan": (
            By.CLASS_NAME, 'hero__line'),
        "my_profile_link": (
            By.CLASS_NAME, 'flex-wrapper'),
        "login_button": (
            By.CLASS_NAME, 'a[href="/oauth-login"]'),
        "logout_button": (
            By.CLASS_NAME, 'a[href="/oauth-signup"]')
    }