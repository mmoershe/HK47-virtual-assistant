import os
import pyautogui 

current_path = os.path.dirname(os.path.abspath(__file__))

pyautogui.screenshot(os.path.join(current_path, "newnewscreenshot.png"))