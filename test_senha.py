from selenium import webdriver

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000")

def limpar_checkboxes():

    for checkbox_id in ["minusculas", "maiusculas", "numeros", "especiais"]:

        checkbox = driver.find_element(By.ID, checkbox_id)

        if checkbox.is_selected():

            checkbox.click()

def gerar():

    driver.find_element(By.XPATH, "//button[contains(text(),'Gerar')]").click()

    time.sleep(1)

def copiar():

    driver.find_element(By.CLASS_NAME, "copiar").click()

    time.sleep(1)

# 🔹 1. Maiúsculas + números

limpar_checkboxes()

driver.find_element(By.ID, "maiusculas").click()

driver.find_element(By.ID, "numeros").click()

gerar()

# 🔹 2. Maiúsculas + minúsculas

limpar_checkboxes()

driver.find_element(By.ID, "maiusculas").click()

driver.find_element(By.ID, "minusculas").click()

gerar()

# 🔹 3. Maiúsculas + símbolos

limpar_checkboxes()

driver.find_element(By.ID, "maiusculas").click()

driver.find_element(By.ID, "especiais").click()

gerar()

# 🔹 4. Minúsculas + números

limpar_checkboxes()

driver.find_element(By.ID, "minusculas").click()

driver.find_element(By.ID, "numeros").click()

gerar()

# 🔹 5. Minúsculas + símbolos

limpar_checkboxes()

driver.find_element(By.ID, "minusculas").click()

driver.find_element(By.ID, "especiais").click()

gerar()

# 🔹 6. Minúsculas + símbolos + copiar

limpar_checkboxes()

driver.find_element(By.ID, "minusculas").click()

driver.find_element(By.ID, "especiais").click()

gerar()

copiar()

# 🔹 7. Minúsculas + símbolos + números + copiar

limpar_checkboxes()

driver.find_element(By.ID, "minusculas").click()

driver.find_element(By.ID, "especiais").click()
driver.find_element(By.ID, "numeros").click()

gerar()

copiar()

# 🔹 8. Todos os checkboxes

limpar_checkboxes()

for checkbox_id in ["minusculas", "maiusculas", "numeros", "especiais"]:

    driver.find_element(By.ID, checkbox_id).click()

gerar()

# 🔹 9. Todos + copiar

copiar()

# 🔹 10. Todos + gerar + copiar

gerar()

copiar()

print("✅ Todos os testes executados!")

time.sleep(3)

driver.quit()