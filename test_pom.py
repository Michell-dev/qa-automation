
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from login_page import LoginPage

def test_login_con_pom():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()

    assert "inventory" in driver.current_url
    driver.quit()