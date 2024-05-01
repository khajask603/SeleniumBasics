from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"F:\Python & Selenium by pavan sir\Drivers\chromedriver.exe")
ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=serv_obj, options=ops)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
Select=driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']")
Select.click()
Names=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']//li")
print(len(Names))

for name in Names:
    if name.text=="Turkey":
     name.click()
     break