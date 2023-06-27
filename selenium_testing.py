from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

myoptions = webdriver.ChromeOptions()
myoptions.binary_location = '/usr/bin/chromium-browser'
driver = webdriver.Chrome("/home/user2/HK47-virtual-assistant/webdriver/chromedriver_linux64/chromedriver")
driver.get("http://www.python.org")
