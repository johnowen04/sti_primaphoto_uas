from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/datapemesanan")
    yield driver
    driver.quit()


def test_admin_terima_bayar(driver):
    driver.find_element(By.NAME, "email").send_keys("admin123@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CLASS_NAME, "btn").click()

    table_pesanan = driver.find_element(
        By.CSS_SELECTOR, "table#table_contoh.table.dataTable")


    row_pesanan = table_pesanan.find_elements(By.CSS_SELECTOR, "tr")[12]
    col_pesanan = row_pesanan.find_elements(By.CSS_SELECTOR, "td")

    button_ubah = col_pesanan[11]

    button_ubah.click()
    time.sleep(1)

    modal_content = driver.find_element(By.CLASS_NAME, "modal-content")
    select = Select(modal_content.find_element(
        By.CSS_SELECTOR, "select#eStatusPembayaran.form-control"))
    select.select_by_visible_text('selesai')
    time.sleep(1)

    modal_footer = driver.find_element(By.CLASS_NAME, "modal-footer")
    button_save = modal_footer.find_element(By.CSS_SELECTOR, "button.btn.btn-info")
    button_save.click()
    time.sleep(1)

    assert "Data pemesanan berhasil di update" in driver.find_element(
        By.CSS_SELECTOR, "div#pesan.alert.alert-success").text
