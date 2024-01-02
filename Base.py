from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import dati
import time

load_dotenv()

# edge_dir = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
edge_dir2 = r'C:\Users\Manuel Luppino\OneDrive - Bit srl\Desktop\msedge.exe'

password_login = os.getenv("PASSWORD_LOGIN")
email_login =os.getenv("EMAIL_LOGIN")

my_options = webdriver.EdgeOptions()
my_options.add_experimental_option('detach', True)
my_options.add_argument(f"user-data-dir={edge_dir2}")
driver = webdriver.Edge(options = my_options)

def open_browser():
    driver.get(dati.bing_url)
    return driver

def first_checks():
    open_browser()
    time.sleep(5)

    try:
        closeCookieButton = driver.find_element(By.ID, 'bnp_btn_reject')
        if closeCookieButton.is_displayed():
            closeCookieButton.click()
    except NoSuchElementException:
            print("Elemento 'bottone rifiuta' non trovato, continuo senza cliccarlo")
    try:
        accedi = driver.find_element(By.ID, 'id_a')
        if accedi.is_displayed():
            accedi.click()
    except NoSuchElementException:
        print("Elemento 'accedi' non trovato, continuo senza cliccarlo")

        time.sleep(3)
        inputEmail = driver.find_element(By.ID, 'i0116')
        inputEmail.send_keys(email_login)
        avantiButton = driver.find_element(By.ID, "idSIButton9")
        avantiButton.click()

        time.sleep(3)
        inputPassword = driver.find_element(By.ID, "i0118")
        inputPassword.send_keys(password_login)
        siButton = driver.find_element(By.ID, "idSIButton9")
        siButton.click()

        time.sleep(3)
        try:
            nonVisualizzarePiuQuestoMessaggio = driver.find_element(By.ID, "KmsiCheckboxField")
            if nonVisualizzarePiuQuestoMessaggio.is_displayed():
                nonVisualizzarePiuQuestoMessaggio.click()
        except NoSuchElementException:
            print("Elemento 'KmsiCheckboxField' non trovato, continuo senza cliccarlo")
        time.sleep(2)
        siButton = driver.find_element(By.ID, "idSIButton9")
        siButton.click()
    
def start_routine():
    try:
        for x in range(35):
            elem = driver.find_element(By.ID, 'sb_form_q')
            elem.clear()
            elem.send_keys(dati.getRandomWord())
            elem.send_keys(Keys.RETURN)
            time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")

first_checks()
start_routine()






