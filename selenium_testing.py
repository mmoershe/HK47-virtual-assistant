from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service = Service("webdriver\\chromedriver_linux64\\chromedriver"))


driver.get("https://www.selenium.dev/selenium/web/web-form.html")