from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://secondhand.binaracademy.org/users/sign_in")

emailfield=driver.find_element(By.XPATH, "//input[@id='user_email']")
emailfield.send_keys("malika@gmail.com")

print("result of text:", emailfield.text)
print("result of get_attribute():",emailfield.get_attribute('value'))

button=driver.find_element(By.XPATH, "//input[@name='commit']")
print("result of get_attribute()", button.get_attribute('value'))
print("result of get_attribute()", button.get_attribute('type'))