from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("msedgedriver.exe")
driver = webdriver.Edge(service=service)
wait = WebDriverWait(driver, 10)

url = "https://webdriveruniversity.com/Contact-Us/contactus.html"


cases = [
    {"first":"Juan", "last":"Pérez", "email":"juan.perez@example.com", "comments":"Formulario válido", "expect":"success"},
    {"first":"Ana", "last":"Lopez", "email":"ana.lopezexample.com", "comments":"Email inválido (sin @)", "expect":"email_error"},
    {"first":"", "last":"Gómez", "email":"maria.gomez@example.com", "comments":"Falta First Name", "expect":"required_error"},
]

for i, case in enumerate(cases, start=1):
    print(f"\n===== Caso {i} | Esperado: {case['expect']} =====")

    driver.get(url)
    driver.maximize_window()

 
    wait.until(EC.presence_of_element_located((By.NAME, "first_name")))
    wait.until(EC.presence_of_element_located((By.NAME, "last_name")))
    wait.until(EC.presence_of_element_located((By.NAME, "email")))
    wait.until(EC.presence_of_element_located((By.NAME, "message")))


    driver.find_element(By.NAME, "first_name").clear()
    driver.find_element(By.NAME, "first_name").send_keys(case["first"])

    driver.find_element(By.NAME, "last_name").clear()
    driver.find_element(By.NAME, "last_name").send_keys(case["last"])

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(case["email"])

    driver.find_element(By.NAME, "message").clear()
    driver.find_element(By.NAME, "message").send_keys(case["comments"])


    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    time.sleep(1.5)


    page_source = driver.page_source.lower()

    if case["expect"] == "success":
        if "thank you" in page_source:
            print("Exito")
        else:
            print("Fallo")

    elif case["expect"] == "email_error":
        if "error" in page_source or "invalid" in page_source:
            print("Exito")
        else:
            print("Fallo")

    elif case["expect"] == "required_error":
        if "error" in page_source:
            print("Exito")
        else:
            print("Fallo")

    time.sleep(1)

print("Ejecución terminada")
print("El navegador queda abierto para revisión manual")

input("Presiona ENTER para cerrar el navegador...")
driver.quit()
