import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

def take_screenshot(context, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_name = os.path.join(screenshot_dir, f"{step_name}_{timestamp}.png")
    context.driver.save_screenshot(screenshot_name)
    context.pdf.add_screenshot(screenshot_name, step_name)
    print(f"Screenshot taken: {screenshot_name}")
    return screenshot_name

def mark_step_as_failed(context, step_name, exception):
    print(f"Error in '{step_name}': {exception}")
    raise Exception(f"Step failed: {step_name}. Error: {exception}")

def mark_step_as_passed(context, step_name):
    print(f"Step passed: {step_name}")

@given('Se inicia el navegador')
def iniciarNavegador(context):
    context.driver = webdriver.Chrome(options=options)
    context.failed_steps = []
    print("Browser started")

@when('Entra a la seccion reporte')
def entrar_seccion_reporte(context):
    try:
        context.driver.maximize_window()
        context.driver.get("C:\\Users\\erick\\Desktop\\ESPE\\QUINTO SEMESTRE\\REQUISITOS\\PRUEBAS-RF\\CU7\\Reporte\\Reporte.html")
        take_screenshot(context, '1. Entra a la seccion reporte')
        print("Entered 'Reporte' section")
    except Exception as e:
        mark_step_as_failed(context, 'entra_seccion_reporte', e)

@when('Llenar el campo ID Viaje {id_viaje}')
def actualizar_id_viaje(context, id_viaje):
    try:
        id_viaje_field = context.driver.find_element(By.XPATH, '//*[@id="idViaje"]')
        id_viaje_field.send_keys(id_viaje)
        take_screenshot(context, '2. Llenar el campo ID Viaje')
    except Exception as e:
        mark_step_as_failed(context, 'actualizar_id_viaje', e)

@when('Aplastar el boton para buscar')
def aplastar_boton_buscar(context):
    try:
        buscar_button = context.driver.find_element(By.XPATH, '//*[@id="lupa"]')
        buscar_button.click()
        time.sleep(5)
        take_screenshot(context, '3. Clickear el boton buscar')
    except Exception as e:
        mark_step_as_failed(context, 'aplastar_boton_buscar', e)

@then('Visualizar reporte viaje')
def verificarReporte(context):
    try:
        # Esperar a que el modal de confirmación aparezca
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="reporte"]'))
        )
        confirmation_message = context.driver.find_element(By.XPATH, '//*[@id="reporte"]/div/div')
        # Si el elemento se encuentra, el paso es exitoso
        time.sleep(5)
        take_screenshot(context, '4. Observar el reporte del viaje')
        mark_step_as_passed(context, 'verificar_reporte')
    except Exception as e:
        # Si ocurre una excepción, el paso falla
        mark_step_as_failed(context, 'verificar_reporte', e)
