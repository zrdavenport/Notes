from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
try:

    browser.get("https://www.amazon.com")
    assert "Amazon" in browser.title

    target = "blender"
    brand = "hamilton beach"

    search_box = browser.find_element_by_id("twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys(target)
    search_box.send_keys(Keys.RETURN)

    results = browser.find_elements_by_class_name("s-result-item")
    n = len(results)
    k = 0
    for results in results:
        if brand.lower() in results.text.lower():
            k += 1
    assert k >= 3
    if k >= 3:
        print("Enough " + brand + " items have been found.")

finally:
    browser.close()