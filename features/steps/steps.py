from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from environment import take_screenshot


@Given('I search for "{query}"')
def step_search_google(context, query):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    take_screenshot(context, query)
    search_box.submit()

@then('I should see "{result}" in the search results')
def step_verify_search_results(context, result):
    assert result in context.driver.page_source