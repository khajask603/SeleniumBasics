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
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
Button=driver.find_element(By.CSS_SELECTOR,".context-menu-one")
act=ActionChains(driver)
act.move_to_element(Button).context_click().perform()           #------->ContextClick (or)RightCLick
editEle=driver.find_element(By.XPATH,"//span[text()='Edit']")
time.sleep(5)
editEle.click()
time.sleep(3)
driver.switch_to.alert.accept()
# //li[contains(@class,'context-menu-icon-edit')]