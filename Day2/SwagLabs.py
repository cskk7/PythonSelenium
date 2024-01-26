from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"F:\chromedriver_win64\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_service = Service()


# LAUNCH BROWSER
driver = webdriver.Chrome(service=chrome_service,options=chrome_options)
driver.get("https://www.saucedemo.com/v1/")

# LOGIN
username = driver.find_element(By.XPATH,"//input[@name='user-name']")
username.send_keys("standard_user")
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys("secret_sauce")
submit = driver.find_element(By.XPATH,"//input[@id='login-button']")
submit.click()

# LOGOUT
navIcon = driver.find_element(By.XPATH,"//button[text()='Open Menu']")
navIcon.click()
driver.implicitly_wait(10)
logoutButton = driver.find_element(By.XPATH,"//a[text()='Logout']")
logoutButton.click()
print("Success")
driver.quit()
