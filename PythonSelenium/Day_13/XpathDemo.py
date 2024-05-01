from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(10)  # Wait up to 10 seconds
driver.get("https://automationexercise.com/products")
# RelativeXpath Sample
driver.find_element(By.XPATH ,"//input[@placeholder='Search Product']").send_keys("Shirts")
driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()

#Xptah with "Or" , "AND"
driver.find_element(By.XPATH,"//*[@id='submit_search' or @class='fa fa-searc']").send_keys("Tops")
driver.find_element(By.XPATH,"//*[@id='submit_search' and @type='button']").click()

# #Xpath with "contains()", "starts-with()"
driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("Jeans")
driver.find_element(By.XPATH,"//button[starts-with(@id,'submit')]").click()

#Xpath with "Text()"
driver.find_element(By.XPATH,"//a[text()=' Products']").click()