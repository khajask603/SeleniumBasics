from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.google.co.in/")
search=driver.find_element(By.ID,"APjFqb")
search.send_keys("Selenium")
search.submit()

# driver.find_element(By.XPATH,"//h3").click()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
driver.quit()
