from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"F:\chromedriver_win64\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_service = Service()

driver = webdriver.Chrome(service=chrome_service,options=chrome_options)

driver.get("https://practicetestautomation.com/practice-test-login/")
username = driver.find_element(By.XPATH,"//input[@name='username']")
username.send_keys("student")
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("Password123")
submit = driver.find_element(By.XPATH,"//button[@id='submit']")
submit.click()

driver.quit()
