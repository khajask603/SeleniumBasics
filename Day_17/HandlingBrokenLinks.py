import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.deadlinkcity.com/")
allLinks=driver.find_elements(By.XPATH,'//a')
count=0
for link in allLinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url, "Is Broken Link")
        count+=1
    else:
        print(url,"Is not an broken link")
print("Total number of broken links:",count)
