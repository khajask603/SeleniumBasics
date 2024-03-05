import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

# Authentication popup
# -----------------------
# http://the-internet.herokuapp.com/basic_auth
# syntax: http://username:password@test.com
# Example: http://admin:admin@the-internet.herokuapp.com/basic_auth

# driver.get("http://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
result=driver.find_element(By.CSS_SELECTOR,".example").text
print(result)       #Basic Auth
                    #Congratulations! You must have the proper credentials.