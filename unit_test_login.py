from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")
    yield driver
    driver.quit()

def test_login_admin(driver):
    driver.find_element(By.NAME, "email").send_keys("admin123@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "btn").click()

    actual_title = driver.title
    expected_title = "Admin Dashboard"

    assert expected_title in actual_title
    
    if (expected_title in actual_title):
        print("Login Admin Test Passed.")
    else:
        print("Login Admin Test Failed.  Actual page: {}".format(actual_title))

def test_login_fotografer(driver):
    driver.find_element(By.NAME, "email").send_keys("fotografer123@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("fotografer123")
    driver.find_element(By.CLASS_NAME, "btn").click()

    actual_title = driver.title
    expected_title = "Fotografer Dashboard"

    assert expected_title in actual_title

    if (expected_title in actual_title):
        print("Login Fotografer Test Passed.")
    else:
        print("Login Fotografer Test Failed.  Actual page: {}".format(actual_title))

def test_login_pelanggan(driver):
    driver.find_element(By.NAME, "email").send_keys("pelanggan1@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("pelanggan1")
    driver.find_element(By.CLASS_NAME, "btn").click()

    actual_title = driver.title
    expected_title = "Pelanggan Dashboard"

    assert expected_title in actual_title

    if (expected_title in actual_title):
        print("Login Pelanggan Test Passed.")
    else:
        print("Login Pelanggan Test Failed. Actual page: {}".format(actual_title))
