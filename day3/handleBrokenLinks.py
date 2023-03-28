from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests as requests

options=webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links=driver.find_elements(By.TAG_NAME, 'a')
count=0

for link in links:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url," is broken")
        count+=1
    else:
        print(url," is valid")

print("Total broken links:", count)