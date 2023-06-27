from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# myoptions = webdriver.ChromeOptions()
# myoptions.binary_location = '/usr/bin/chromium-browser'
path_chromium = "/usr/lib/chromium-browser/chromedriver"
driver = webdriver.Chrome()
driver.get("http://www.python.org")
