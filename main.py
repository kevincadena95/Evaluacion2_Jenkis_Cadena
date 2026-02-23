from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

service = Service("msedgedriver.exe")
driver = webdriver.Edge(service=service)
wait = WebDriverWait(driver, 8)

BASE_URL = "https://webdriveruniversity.com/Contact-Us/contactus.html"

cases = [
    ("TC01", "Juan", "Pérez", "juan.perez@example.com", "Comentario válido", "success"),
    ("TC02", "Ana", "García", "email-invalido", "Email inválido", "error"),
    ("TC03", "Luis", "Lopez", "luis.lopez@example.com", "", "error"),  # falta comments
]

def abrir():
    driver.get(BASE_URL)
    wait.until(EC.presence_of_element_located((By.NAME, "first_name")))

def enviar(first, last, email, comments):
    driver.find_element(By.NAME, "first_name").clear(); driver.find_element(By.NAME, "first_name").send_keys(first)
    driver.find_element(By.NAME, "last_name").clear();  driver.find_element(By.NAME, "last_name").send_keys(last)
    driver.find_element(By.NAME, "email").clear();      driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "message").clear();    driver.find_element(By.NAME, "message").send_keys(comments)
    driver.find_element(By.XPATH, "//input[@value='SUBMIT']").click()

def check_success():
    try:
        h = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#contact_reply h1")))
        return "Thank You for your Message!" in h.text
    except TimeoutException:
        return False

def check_error():
    try:
        body = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))).text
        return ("Error: Invalid email address" in body) or ("Error: all fields are required" in body)
    except TimeoutException:
        return False

results = []
try:
    for tc_id, first, last, email, comments, expected in cases:
        abrir()
        enviar(first, last, email, comments)
        # breve espera para que responda el servidor
        time.sleep(0.5)
        if expected == "success":
            passed = check_success()
        else:
            passed = check_error()
        results.append((tc_id, passed))
        print(f"{tc_id} -> {'PASS' if passed else 'FAIL'}")
finally:
    print("\nResumen:")
    for r in results:
        print(f"{r[0]}: {'PASS' if r[1] else 'FAIL'}")
    time.sleep(1)
    driver.quit()