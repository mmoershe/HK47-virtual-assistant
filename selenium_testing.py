from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.binary_location = '/usr/bin/chromium-browser'

driver = webdriver.Chrome('webdriver/chromedriver_linux64/chromedriver')

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

print(driver.title)