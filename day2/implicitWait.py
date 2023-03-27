from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

driver.get("https://www.google.co.id")
driver.maximize_window()

search=driver.find_element(By.NAME, 'q')
search.send_keys("Selenium")
search.submit()

driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()

driver.quit()