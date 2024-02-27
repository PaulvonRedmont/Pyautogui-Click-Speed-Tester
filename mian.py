import pyautogui
import time

start_time = time.time()

# Perform the click operation
pyautogui.click()

end_time = time.time()

click_duration = end_time - start_time
print("Click duration:", click_duration, "seconds")
