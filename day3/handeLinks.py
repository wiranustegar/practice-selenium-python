from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#click link text
# driver.find_element(By.LINK_TEXT, "Apparel").click()

#test
#test

#links in a page
links=driver.find_elements(By.XPATH, "//a")
print("Number of links:", len(links))

for link in links:
    print(link.text)