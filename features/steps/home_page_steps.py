from behave import *
from nose.tools import assert_equals, assert_true
import re


@given('I am redirected on home page')
def navigate_to_home_page(context):
    assert_equals(context.browser.current_url, "{}".format(
        context.home_page.project_url))


@step('In home page I want to see {element_name}')
def check_element_on_home_page(context, element_name):
    can_see = context.home_page.wait_till_specific_element_is_not_displayed(
        context.home_page.local_directories[element_name])
    assert_true(can_see, "Element {} displayed on the page in the implicit time window".format(element_name))


@step('In searching page I want to see {element_name}')
def check_element_on_home_page(context, element_name):
    can_see = context.searching_page.wait_till_specific_element_is_not_displayed(
        context.searching_page.local_directories[element_name])
    assert_true(can_see, "Element {} displayed on the page in the implicit time window".format(element_name))


@step('On page I want to see {element_name}')
def check_element_on_search_bar(context, element_name):
    can_see = context.search_bar.wait_till_specific_element_is_not_displayed(
        context.search_bar.local_directories[element_name])
    assert_true(can_see, "Element {} displayed on the page in the implicit time window".format(element_name))


@step('I click on {where} in search bar')
def click_on_element_in_search_bar(context, where):
    context.search_bar.click_on_element(where)


@when ('I want to see {text} in {element}')
def get_text_from_element(context, text, element):
    element_text = context.home_page.get_text_from_element(element)
    assert re.search(text, element_text)