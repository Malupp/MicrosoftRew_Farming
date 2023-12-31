from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import data
import time



my_options = webdriver.EdgeOptions()
my_options.add_experimental_option('detach', True)
my_options.add_argument(f"user-data-dir={data.edge_dir2}")
driver = webdriver.Edge(options = my_options)

# It will open the browser with a default URL I chose
def open_browser():
    driver.get(data.bing_url)
    return driver

def first_checks():
    open_browser()
    time.sleep(5)

    # It will close the button "rifiuta" if present
    try:
        closeCookieButton = driver.find_element(By.ID, 'bnp_btn_reject')
        if closeCookieButton.is_displayed():
            closeCookieButton.click()
    except NoSuchElementException:
            print("Elemento 'bottone rifiuta' non trovato, continuo senza cliccarlo")

    # It will click the button "accedi" if you are not enrolled
    try:
        accedi = driver.find_element(By.ID, 'id_a')
        if accedi.is_displayed():
            accedi.click()
    except NoSuchElementException:
        print("Elemento 'accedi' non trovato, continuo senza cliccarlo")

    # It will try to login at this point with your information
        time.sleep(3)
        inputEmail = driver.find_element(By.ID, 'i0116')
        inputEmail.send_keys(data.email_login)
        avantiButton = driver.find_element(By.ID, "idSIButton9")
        avantiButton.click()

        time.sleep(3)
        inputPassword = driver.find_element(By.ID, "i0118")
        inputPassword.send_keys(data.password_login)
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

# This function will search 50 random words to farm points
def start_routine():
    try:
        for x in range(50):
            elem = driver.find_element(By.ID, 'sb_form_q')
            elem.clear()
            elem.send_keys(data.getRandomWord())
            elem.send_keys(Keys.RETURN)
            time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")

def open_tasks():
    button_tasks = driver.find_element(By.ID, 'id_rh').click()
    return button_tasks

first_checks()
start_routine()






