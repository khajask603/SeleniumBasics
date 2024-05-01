from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

#----------------------- find_element() - Returns single webelement---------------------
#1)Locator matching with single webelement
elemet=driver.find_element(By.CSS_SELECTOR,"#small-searchterms")
elemet.send_keys("Apple MacBook Pro 13-inch")

#2) Locator matching with multiple webelements
elements=driver.find_element(By.XPATH,"//div[@class='footer-upper']//a")
print(elements.text)     #Sitemap-------      #prints first link from the footer "Sitemap"

#3) Element not available then throw NoSuchElementException
elemnent3=driver.find_element(By.LINK_TEXT,"login")
elemnent3.click()    #selenium.common.exceptions.NoSuchElementException: Message

#---------------------------------#######   find_elements() - Returns multiple webElements---------------
#1)Locator matching with single webelement--
elemet=driver.find_elements(By.CSS_SELECTOR,"#small-searchterms")
print(len(elemet))                                #---1
elemet[0].send_keys("Apple MacBook Pro 13-inch")
#2) Locator matching with multiple webelements
elements=driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
print(len(elemet))                                #---1
for ele in elements:
    print(ele.text) #-->Print all of the Element avialble on the list for locatore
#3) Element not available - zero
elemnent3=driver.find_elements(By.LINK_TEXT,"login")
print(len(elemnent3))                            #--- 0