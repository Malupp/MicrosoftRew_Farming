#TODO Da completare integrando pyautogui
def click_accedi(x, y):
    window_size = driver.get_window_size()
    actual_x = int(window_size['width'] * (x / 100))
    actual_y = int(window_size['height'] * (y / 100))
    print(window_size)
