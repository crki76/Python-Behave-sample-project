from behave import *
from nose.tools import assert_true


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
    context.searching_page.wait_till_specific_element_is_not_displayed(
        context.searching_page.local_directories[element])
    context.searching_page.click_on_element(element)


@step('I check if my {is_selected} is selected')
def is_it_selected(context, is_selected):
    context.searching_page.wait_till_specific_element_is_not_displayed(
        context.searching_page.local_directories["item_details"])
    check_it = context.searching_page.is_element_exists(is_selected)
    assert_true(check_it)