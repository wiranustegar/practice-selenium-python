from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_displayed() -- is_enabled()
emailfield = driver.find_element(By.XPATH, "//input[@id='Email']")
print("Display Status:", emailfield.is_displayed())
print("Enable Status:", emailfield.is_enabled())

#is_selected() for radio buttons and checkboxes
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("Default radio button")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()

print("[After click male radio button]")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_female.click()

print("[After click female radio button]")
print(rd_male.is_selected())
print(rd_female.is_selected())


driver.quit()