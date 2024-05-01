import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
driver.close()               #To stop specifdic window
time.sleep(2)
driver.quit()               #to cloase all browser tab