import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "F:\\chromedriver_win64\\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get("http://www.google.com")
search_box = driver.find_element("name", "q")
search_box.send_keys("codoid innovations")
search_box.send_keys(Keys.RETURN)
time.sleep(2)
print("Title: " + driver.title)
driver.quit()