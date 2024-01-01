from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from data import getRandomWord, bing_url
import time


# edge_dir = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

def start_routine():
    try:
        # Create WebDriver
        driver = webdriver.Edge()
        # Navigate to URL
        driver.get(bing_url)
        options = webdriver.EdgeOptions()
        # Let the tab up
        options.add_experimental_option("detach", True)
        for x in range(30):
            elem = driver.find_element(By.ID, 'sb_form_q')
            elem.clear()
            elem.send_keys(getRandomWord())
            elem.send_keys(Keys.RETURN)
            time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")

start_routine()






