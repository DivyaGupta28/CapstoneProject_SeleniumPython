# Capstone project using selenium with python (use pytest framework) and use fixtures
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webbrowser import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Fixture to setup and teardown WebDriver
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# Test to verify the title of the page
def test_verify_homepage_title(driver):
    driver.get("http://the-internet.herokuapp.com/")
    assert driver.title == "The Internet", "Title does not match"

# Test to verify Checkboxes functionality
def test_checkboxes(driver):
    driver.find_element(By.LINK_TEXT, "Checkboxes").click()
    assert driver.find_element(By.TAG_NAME, "h3").text == "Checkboxes", "Heading does not match"
    
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    assert not checkboxes[0].is_selected(), "Checkbox 1 should not be checked"
    assert checkboxes[1].is_selected(), "Checkbox 2 should be checked"
    
    driver.back()
    time.sleep(5)

# Test to verify File Upload functionality
def test_file_upload(driver):
    driver.find_element(By.LINK_TEXT, "File Upload").click()
    assert driver.find_element(By.TAG_NAME, "h3").text == "File Uploader", "Heading does not match"
    
    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys("/Users/divyagupta/Downloads/testfile.docx")  # Change this path to an actual file on your system
    
    driver.find_element(By.ID, "file-submit").click()
    time.sleep(5)
    
    assert "File Uploaded!" in driver.page_source, "File upload failed"
