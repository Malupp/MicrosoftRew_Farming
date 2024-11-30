from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
import dati
import time

load_dotenv()

## Qui inserisci il path di dove si trova l'exe di Edge, consiglio: Creare un collegamento su una cartella desktop e incollare quel path qui

### Es. Questo qui sotto non funzionerà
# edge_dir = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

### Questi qui sotto invece funzionano perché sono dei path-collegamenti su una cartella creata appositamente

# edge_dir2 = r'C:\Users\Utente 1\Documents\Microsoft rewards browser'
# edge_dir3 = r'C:\Users\Manuel Luppino\OneDrive - Bit srl\Desktop\msedge.exe'
edge_dir4 = r'C:\Users\Admin\Desktop\Coding Project\msedge.exe'

password_login = os.getenv("PASSWORD_LOGIN")
email_login =os.getenv("EMAIL_LOGIN")

my_options = webdriver.EdgeOptions()
my_options.add_experimental_option('detach', True)
my_options.add_argument(f"user-data-dir={edge_dir4}")
driver = webdriver.Edge(options = my_options)

def open_browser():
    driver.get(dati.bing_url)
    return driver

def first_checks():
    open_browser()
    time.sleep(5)

    # try:
    #     closeCookieButton = driver.find_element(By.ID, 'bnp_btn_reject')
    #     if closeCookieButton.is_displayed():
    #         closeCookieButton.click()
    # except NoSuchElementException:
    #         print("Elemento 'bottone rifiuta' non trovato, continuo senza cliccarlo")
    # try:
    #     accedi = driver.find_element(By.ID, 'id_a')
    #     if accedi.is_displayed():
    #         accedi.click()
    # except NoSuchElementException:
    #     print("Elemento 'accedi' non trovato, continuo senza cliccarlo")

    #     time.sleep(3)
    #     inputEmail = driver.find_element(By.ID, 'i0116')
    #     inputEmail.send_keys(email_login)
    #     avantiButton = driver.find_element(By.ID, "idSIButton9")
    #     avantiButton.click()

    #     time.sleep(3)
    #     inputPassword = driver.find_element(By.ID, "i0118")
    #     inputPassword.send_keys(password_login)
    #     siButton = driver.find_element(By.ID, "idSIButton9")
    #     siButton.click()

    #     time.sleep(3)
    #     try:
    #         nonVisualizzarePiuQuestoMessaggio = driver.find_element(By.ID, "KmsiCheckboxField")
    #         if nonVisualizzarePiuQuestoMessaggio.is_displayed():
    #             nonVisualizzarePiuQuestoMessaggio.click()
    #     except NoSuchElementException:
    #         print("Elemento 'KmsiCheckboxField' non trovato, continuo senza cliccarlo")
    #     time.sleep(2)
    #     siButton = driver.find_element(By.ID, "idSIButton9")
    #     siButton.click()

def start_routine():
    try:
        for x in range(35):
            elem = driver.find_element(By.ID, 'sb_form_q')
            elem.clear()
            elem.send_keys(dati.getRandomWord())
            elem.send_keys(Keys.RETURN)
            time.sleep(6)

        current_points = get_points()
        if current_points is not None and current_points < 90:
            print(f"Not enough points ({current_points}), continuing search.")
            start_routine()
        else:
            print(f"Reached 90 points ({current_points}), stopping search.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_points():
    try:
        btnMissions = driver.find_element(By.ID, 'rh_meter')
        btnMissions.click()
        time.sleep(3)
        points_element = driver.find_element(By.CLASS_NAME, 'b_subtitle.promo-title')
        points_text = points_element.text.strip()
        points = int(points_text.split()[0])
        return points
    except NoSuchElementException:
        print("Points element not found")
        return None
    except ValueError:
        print("Unable to convert points to an integer")
        return None

def CheckQuests():
    try:
        promo_elements = driver.find_elements(By.TAG_NAME, 'promo_cont')

        for e in promo_elements:
            print(e.text)
    except ValueError:
        print("Unable to convert points to an integer")
        return None

first_checks()
start_routine()
