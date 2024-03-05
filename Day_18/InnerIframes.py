from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

OuterFrame=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(OuterFrame)

InnerFrame=driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(InnerFrame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")
driver.switch_to.default_content()