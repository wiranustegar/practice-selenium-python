from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# country=driver.find_element(By.XPATH, "//select[@class='custom-select']")
country=Select(driver.find_element(By.XPATH, "//select[@class='custom-select']"))

#select by visible text
# country.select_by_visible_text("Italy")

#select by value
country.select_by_value("2")

#print all the option
alloptions=country.options
print("Total number of options:", len(alloptions))

for nameOptions in alloptions:
    print(nameOptions.text)