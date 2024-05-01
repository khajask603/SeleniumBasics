from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()
