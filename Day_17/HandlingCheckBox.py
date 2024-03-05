from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
# A) select specific checkbox
driver.find_element(By.XPATH,"//input[@id='monday']").click()

#-----------------------------------------------------------------------
#B) select all the checkboxes
cBoxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(cBoxes))

#-------Approach -1------USing Range Fucntion---------------
for i in range(len(cBoxes)):
    cBoxes[i].click()

#-------Approach -2---------------------
for cb in cBoxes:
    cb.click()  #Unselected which are selected in Approach-1

#-------Approach -3 ------select multiple checkboxes by choice---------
for cb in cBoxes:
    weekName=cb.get_attribute('value')
    if weekName=='monday' or weekName=='sunday':
        cb.click()
    print(weekName, cb.is_selected())  # Print the weekName and its selected state #2

#Appraoch-4 ) -------select last 2 checkboxes----------------
for i in range(len(cBoxes)-2,len(cBoxes)):
    cBoxes[i].click()                #Friday,saruday selectted

#Appraoch-5 ) -------select First 2 checkboxes----------------
for i in range(len(cBoxes)):
    if i<2:
        cBoxes[i].click()          #Sunday , munday seleced

#Appraoch-6)------------- clearing all the check boxes-----------------
for cb in cBoxes:
    if cb.is_selected():
        cb.click()

driver.quit()