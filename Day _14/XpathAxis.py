from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(10)  # Wait up to 10 seconds
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

##----Self-------
self=driver.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels')]").text
print(self)

#-----Parent----------
Parent=driver.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels')]//parent::td").text
print(Parent)

#----Child-----------------
child=driver.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels C')]/ancestor::tr/child::td").text
print(child)
#--Ancestor-----------
Ances=driver.find_element(By.XPATH,"//a[contains(text(),'Indian Hotels C')]/ancestor::tr").text
print(Ances)
#--Descendant-----------
Desc=driver.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels C')]/ancestor::tr/descendant::*")
print(len(Desc))
#--Following-----------
flow=driver.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels C')]/ancestor::tr/following::*")
print(len(flow))

#--Preceding-----------
Pres=driver.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels C')]/ancestor::tr/preceding::*")
print(len(Pres))
#--Following Sibiling-----------
flSi=driver.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels C')]/ancestor::tr/following-sibling::tr/td/a")
print(len(flSi))
#--Precsding Sibiling-----------
prSi=driver.find_elements(By.XPATH,"//a[contains(text(),'Indian Hotels C')]/ancestor::tr/preceding-sibling::tr/td/a")
print(len(prSi))