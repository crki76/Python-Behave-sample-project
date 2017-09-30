from behave import *
from nose.tools import assert_true, assert_equals
import time


@step('I insert {insert_text} to search bar')
def insert_text(context, insert_text):
    context.search_bar.wait_till_specific_element_is_not_displayed(
        context.search_bar.local_directories["searching_bar"])
    context.search_bar.insert_text_to_search_bar(insert_text)


@step('I ensure that {inserted_text} is in {element}')
def check_text_in_the_element(context, inserted_text, element):
    element_text = context.search_bar.get_attr_value(element)
    assert(inserted_text in element_text)


@then('I click on searching_button in search bar')
def click_search_button(context):
    context.search_bar.click_on_element("searching_button")


@step('I click on {element}')
def click_search_button(context, element):
    time.sleep(5)
    context.searching_page.wait_till_specific_element_is_not_displayed(
        context.searching_page.local_directories[element])
    context.searching_page.click_on_element(element)


@step('I check if my {is_selected} is selected')
def is_it_selected(context, is_selected):
    check_it = context.searching_page.is_element_exists(is_selected)
    assert_true(check_it)


@step('I expect {result} in {element} for my searching of {inserted_text} and {option}')
def final_searching_page_assertion(context, result, element, inserted_text, option):
    container = context.searching_page.get_attr_title(element)
    if inserted_text in container:
        print("Searched object {} with option {} has been found".format(inserted_text, option))
        search_result = "True"
    else:
        print("Object {} with option {} could not be found".format(inserted_text, option))
        search_result = "False"
    assert_equals(search_result, result)