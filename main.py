from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service("msedgedriver.exe")
drive = webdriver.Edge(service=service)

drive.get("https://webdriveruniversity.com/Contact-Us/contactus.html")
drive.maximize_window()

WebDriverWait(drive, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
    )

username_input = drive.find_element(By.XPATH, "//input[@placeholder='Username']")
username_input.send_keys("standard_user")

password_input = drive.find_element(By.XPATH, "//input[contains(@name,'password')]")
password_input.send_keys("secret_sauce")

time.sleep(4)

login_button = drive.find_element(By.XPATH, "//*[@id='login-button']")
login_button.click()


WebDriverWait(drive, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'T-shirt')]/../../..//button"))
    )

boton_agregar = drive.find_element(By.XPATH, "//div[contains(text(), 'T-shirt')]/../../..//button")
boton_agregar.click()

WebDriverWait(drive, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Onesie')]/../../..//button"))
    )

boton_agregar = drive.find_element(By.XPATH, "//div[contains(text(), 'Onesie')]/../../..//button")
boton_agregar.click()

WebDriverWait(drive, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Jacket')]/../../..//button"))
    )

boton_agregar = drive.find_element(By.XPATH, "//div[contains(text(), 'Jacket')]/../../..//button")
boton_agregar.click()

WebDriverWait(drive, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Backpack')]/../../..//button"))
    )

boton_agregar = drive.find_element(By.XPATH, "//div[contains(text(), ' Backpack')]/../../..//button")
boton_agregar.click()

time.sleep(12)
