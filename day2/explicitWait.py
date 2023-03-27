from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

mywait=WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, Exception])

driver.get("https://www.google.co.id")
driver.maximize_window()

search=driver.find_element(By.NAME, 'q')
search.send_keys("Instagram")
search.submit()

searchLink=mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Instagram']")))
searchLink.click()

driver.quit()