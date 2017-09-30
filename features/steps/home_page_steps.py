from behave import *
from nose.tools import assert_equals, assert_true


@given('I am redirected on home page')
def navigate_to_home_page(context):
    assert_equals(context.browser.current_url, "{}".format(
        context.home_page.project_url))


@step('I want to see {element_name}')
def check_element_on_home_page(context, element_name):
    can_see = context.home_page.wait_till_specific_element_is_not_displayed(
        context.home_page.local_directories[element_name])
    assert_true(can_see, "Element {} displayed on the page in the implicit time window".format(element_name))


@step('I click on {where} in home page')
def click_on_element_in_home_page(context, where):
    context.home_page.click_on_element(where)