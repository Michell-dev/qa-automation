from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_checkout_completo():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    espera = WebDriverWait(driver, 10)
    espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    driver.get("https://www.saucedemo.com/checkout-step-one.html")
    espera.until(EC.visibility_of_element_located((By.ID, "first-name")))

    driver.find_element(By.ID, "first-name").send_keys("Michell")
    driver.find_element(By.ID, "last-name").send_keys("Dev")
    driver.find_element(By.ID, "postal-code").send_keys("80000")
    driver.find_element(By.ID, "continue").click()

    espera.until(EC.url_contains("checkout-step-two"))
    driver.find_element(By.ID, "finish").click()

    espera.until(EC.url_contains("checkout-complete"))
    confirmacion = driver.find_element(By.CLASS_NAME, "complete-header")
    assert confirmacion.text == "Thank you for your order!"

    driver.quit()