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
driver.get("https://demo.nopcommerce.com/")

#----------ID & Name Locatores---------
driver.find_element(By.ID,"small-searchterms").send_keys("Lumia")      #ID -Locator
# driver.find_element(By.NAME,"q").send_keys("Lumia")                       #Name-Locatore

#----------Link Text & Partial Link Textr Locatores---------
driver.find_element(By.LINK_TEXT,"Shopping cart").click()                   #Link text -Locator
driver.find_element(By.PARTIAL_LINK_TEXT,"Shopping ").click()            #Partial Link text -Locator
#Tagname --class name locatore-------------
linkCount=driver.find_elements(By.TAG_NAME,"a")                     #Tagname
print(len(linkCount))                                  #86
