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
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
act=ActionChains(driver)

#Rome-->Italy
source=driver.find_element(By.ID,"box6")
dest=driver.find_element(By.ID,"box106")
act.drag_and_drop(source,dest).perform()

#Washingtom  -->A<merica
source2=driver.find_element(By.ID,"box3")
dest2=driver.find_element(By.ID,"box103")
act.drag_and_drop(source2,dest2).perform()