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
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
frame1=driver.switch_to.frame("iframeResult")
field1=driver.find_element(By.ID,"field1")
field1.clear()
field1.send_keys("Welcome")

Act=ActionChains(driver)
button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
Act.double_click(button).perform()
