from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = '/usr/bin/chromium-browser'

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Specify the relative path to the Chromedriver
driver_path = os.path.join(current_dir, 'chromedriver')


driver = webdriver.Chrome(driver_path, options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

print(driver.title)