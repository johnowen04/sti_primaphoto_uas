from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/jadwalfotografer")
    yield driver
    driver.quit()


def test_admin_jadwal_fotografer(driver):
    driver.find_element(By.NAME, "email").send_keys("admin123@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(1)

    button_tambah = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-info")
    button_tambah.click()
    time.sleep(1)

    select_detail = Select(driver.find_element(By.NAME, "detail_pemesanans_id"))
    select_detail.select_by_value('1')
    time.sleep(1)

    select_name = Select(driver.find_element(By.NAME, "data_fotografers_id"))
    select_name.select_by_value('1')
    time.sleep(1)

    select_admin = Select(driver.find_element(By.NAME, "admin_studios_id"))
    select_admin.select_by_value('1')
    time.sleep(1)

    select_status = Select(driver.find_element(By.NAME, "status"))
    select_status.select_by_visible_text('selesai')
    time.sleep(1)

    button_suubmit = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-info")
    button_suubmit.click()
    time.sleep(1)

    assert "Jadwal fotografer baru berhasil tersimpan" in driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success").text
