from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_agregar_al_carrito():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    espera = WebDriverWait(driver, 10)
    espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador.text == "1"

   driver.quit()

   
