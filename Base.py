from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Arrays import word_list, bing_url
import time
import pyautogui

# edge_dir = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

driver = None

#TODO Da completare integrando pyautogui
def click_accedi(x, y):
    window_size = driver.get_window_size()
    actual_x = int(window_size['width'] * (x / 100))
    actual_y = int(window_size['height'] * (y / 100))
    print(window_size)

def start_routine(word_list, bing_url):
    global driver
    try:
        # Create a WebDriver
        driver = webdriver.Edge()
        # Navigate to URL
        driver.get(bing_url)
        options = webdriver.EdgeOptions()
        # Let the tab up
        options.add_experimental_option("detach", True)
        for word in word_list:
            elem = driver.find_element(By.ID, 'sb_form_q')

        # Open a new window
        driver.execute_script(f"window.open('{bing_url}', '_blank');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(bing_url)
        elem.clear()
        elem.send_keys(word)
        elem.send_keys(Keys.RETURN)
        time.sleep(4)
    except Exception as e:
        print(f"An error occurred: {e}")

start_routine(word_list, bing_url)






