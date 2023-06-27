from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = '/usr/bin/chromium-browser'  # Path to Chromium binary
driver_path = 'webdriver/chromedriver_linux64/chromedriver'  # Path to Chromedriver

driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

print(driver.title)