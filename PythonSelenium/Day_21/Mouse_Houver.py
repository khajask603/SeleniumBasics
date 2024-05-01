from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
act=ActionChains(driver)
head=driver.find_element(By.ID,"mousehover")
tailClick=driver.find_element(By.XPATH,"//a[normalize-space()='Reload']")
act.move_to_element(head).move_to_element(tailClick).click().perform()


