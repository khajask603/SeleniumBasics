import requests
from selenium.webdriver.support.select import Select
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
ddElemnt=driver.find_element(By.XPATH,"//select[@id='country']")
#----------Using Select Class----
dD=Select(ddElemnt)
# dD.select_by_visible_text("India")
# dD.select_by_value('france')
dD.select_by_index(5)          #Australia
# print(ddElemnt.text) #-->it will ghive avilable names list by printing
# Retrieving the selected option text
selected_option = dD.first_selected_option.text
print(selected_option) #-->it will give seleced names list by printing

# capture all the options and print them-----------------------
# Using OptionsMehtod to exteracxt text
allOptions=dD.options
print("Total Number of Options",len(allOptions))      #---->10


for opt in allOptions:
    print(opt.text)
# B) Approach -2---------
# select option from dropdown without using built-in method
for opt in allOptions:
    if opt=='India':
        opt.click()
        break
opns=driver.find_elements(By.XPATH,"//select[@id='country']/option")
print(len(opns))          #-------->10