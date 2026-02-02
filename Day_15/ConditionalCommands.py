from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
iPBox=driver.find_element(By.CSS_SELECTOR,"#name")
print("Input Box is Displayed :-",iPBox.is_displayed())
print("Input Box is Displayed :-",iPBox.is_enabled())

#-------IS Selected()------
rB1=driver.find_element(By.CSS_SELECTOR,"input[value='radio1']")
rB2=driver.find_element(By.CSS_SELECTOR,"input[value='radio2']")

print(rB1.is_selected())     #False Expected
print(rB2.is_selected())     #False Expected
rB3=driver.find_element(By.XPATH,"//input[@value='radio3']")
rB3.click()
print(rB3.is_selected(),"Radio button Is Selected")
#Checkbox,--Selected,enabled,displayed
cKBox=driver.find_element(By.CSS_SELECTOR,"#checkBoxOption2")
print("Check Box is Displayed :-",cKBox.is_displayed())
print("Check Box is Displayed :-",cKBox.is_enabled())
cKBox2=driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").click()
print(cKBox2.is_selected(),"Check box button Is Selected")
