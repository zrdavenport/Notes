import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "http://localhost:5000"

def test_home_page_exists():
    print("\ntesting home page exists")
    response = requests.get(url + "/notes")
    assert response.status_code == 200
    assert response.text > ""
    assert "<HTML>" in response.text.upper()

def test_home_page_has_submit_button():
    print("\ntesting home page has submit button")
    response = requests.get(url + "/notes")
    assert response.status_code == 200
    assert "<input type=\"submit\"" in response.text.lower().replace(" ","")
    soup = BeautifulSoup(response.text, "html.parser")
    inputs = soup.find_all("input")
    submit_inputs = [input for input in inputs if input['type'] == "submit"]
    assert len(submit_inputs) > 0
    for input in submit_inputs:
        assert input["value"] == "Submit"

def test_home_page_submits_data_into_list():
    print("\ntesting home page submits data into a list")
    browser = webdriver.Chrome()
    browser.get(url=url + '/notes')
    input_box = browser.find_element_by_name("note")
    input_box.clear()
    input_box.send_keys("n=", str(time.time()))

    submit_button = browser.find_element_by_id("submit_button")
    submit_button.click()

    time.sleep(10)
    browser.close()