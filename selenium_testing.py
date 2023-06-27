from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/chromium-browser'
driver = webdriver.Chrome("/home/user2/HK47-virtual-assistant/webdriver/chromedriver_linux64/chromedriver", options=options)
driver.get("http://www.python.org")
