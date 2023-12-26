from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

bing_url = "https://www.bing.com/search?q=ss&form=QBLH&sp=-1&ghc=1&lq=0&pq=ss&sc=11-2&qs=n&sk=&cvid=133DE369E02F41CCA18BB28FBF10660F&ghsh=0&ghacc=0&ghpl="

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
driver.get(bing_url)


def click_accedi(x, y):
    window_size = driver.get_window_size()
    actual_x = int(window_size['width'] * (x / 100))
    actual_y = int(window_size['height'] * (y / 100))
    print(window_size)


word_list = ["videogiochi", "programming", "machine", "learning", "python", "example", "random", "words", "selenium", "browser", "automation", "testing", "web", "driver", "element", "key", "by", "ID", "options", "detach", "execute", "submit", "form", "search", "Bing", "Google", "Yahoo", "website", "link", "click", "navigate", "navigate", "back", "forward", "refresh", "close", "open", "session"]

for word in word_list:
    # closeCookie = driver.find_element(By.ID, 'bnp_btn_reject')
    # if closeCookie.is_displayed():
    #     closeCookie.send_keys(Keys.RETURN)
    # else :
        elem = driver.find_element(By.ID, 'sb_form_q')
        elem.clear()
        elem.send_keys(word)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

# driver.close()
