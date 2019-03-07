from behave import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = None

@given(u'we are at {url}')
def step_impl(context, url):
    context.browser = webdriver.Chrome()
    context.browser.get(url)


@when(u'we enter a new note containing {text}')
def step_impl(context, text):
    note_text_box = context.browser.find_element_by_id("note_text")
    note_text_box.clear()
    note_text_box.send_keys(text)

@when(u'we submit the note')
def step_impl(context):
    submit_button = context.brower.find_element_by_id("submit_button")
    submit_button.click()

@then(u'we will get some notes in results')
def step_impl(context):
    content_div = context.brower.find_element_by_id("content")
    content_table = content_div.find_element_by_id("table")
    context.content_rows = content_table.find_elements_by_id("tr")
    assert len(context.content_rows) > 0
        

@then(u'the list will contain {text}')
def step_impl(context, text):
    assert context.content_rows
    for row in context.content_rows:
        if text in row:
            return
    assert False, "text doesn't appear in content"