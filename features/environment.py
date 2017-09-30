from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from features.pages.home_page import HomePage
import inspect



# def load_json(json_file):
#     data = load_file(json_file)
#     json_data = json.loads(data)
#     return json_data
#
#
# def load_file(filename):
#     with open(filename, 'r') as f:
#         data = f.read()
#     return data
#
#
#
#
# def before_all(context):
#     context.env_file = "./myfile.json"
#     context.env = load_json(context.env_file)
#     if "location" in context.env.keys():
#         context.location = context.env["location"]["url"]
#         a = context.location
#         print(a)





def before_scenario(context, scenario):
    context.location = "https://www.trivago.ie"
    context.browser = webdriver.Chrome('/home/crki/git/kneat/chromedriver')
    #context.browser.get("www.zoznam.sk")
    context.browser.get(context.location)

    context.home_page = HomePage(
        context.browser, context.location)


def wait_for_clickable_element(context, id_name):
    try:
        wait = WebDriverWait(context.browser, 15)
        expected_element = EC.element_to_be_clickable(By.ID, id_name)
        wait.until(expected_element)
    except TimeoutError:
        raise


def return_id_name(tuple_id):
    try:
        id, element_name = tuple_id
        return element_name
    except ValueError:
        raise


def clickable_element_process(context, tuple):
    try:
        element_id = return_id_name(tuple)
        wait_for_clickable_element(context, element_id)
    except Exception as e:
        print(e)