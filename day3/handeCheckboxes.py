from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

#specific checkboxes
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

#multiple checkboxes
checkboxes=driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#select multicheckboxes
for checkbox in checkboxes:
    namaHari=checkbox.get_attribute('id')
    if namaHari=='monday' or namaHari=='friday':
        checkbox.click()

# driver.quit()