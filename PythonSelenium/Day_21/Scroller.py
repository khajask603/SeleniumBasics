import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://history.state.gov/countries/all")

#--------------------APPROACH-1-# 1. Scroll down page by pixel------------------

driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) #3000

#2. Scroll down page till the element is visible---------Using JAVASCRITP ------------------------------
flag=driver.find_element(By.LINK_TEXT,"India")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)                      #Number of pixels moved: 4089.333251953125

# #3.scroll down page till end------------------------------------------------------------------
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)                             #-Number of pixels moved: 5182
time.sleep(5)
#
# #4.)Scroll up to starting position------------------------------------

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)                                #Number of pixels moved: 0
