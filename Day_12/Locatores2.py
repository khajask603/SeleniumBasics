from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# service_obj = Service("F:\\Python & Selenium by pavan sir\\Drivers\\chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service_obj, options=options)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(10)  # Wait up to 10 seconds
driver.get("https://automationexercise.com/")
sliders=driver.find_elements(By.CLASS_NAME,"item")
print(len(sliders))

#Tagname --class name locatore-------------
sliders=driver.find_elements(By.CLASS_NAME,"item")                  #classname
print(len(sliders))

linkCount=driver.find_elements(By.TAG_NAME,"a")                     #Tagname
print(len(linkCount))                                  #86
