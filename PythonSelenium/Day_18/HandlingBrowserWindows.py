import time
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
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.PARTIAL_LINK_TEXT,"OrangeHRM").click()
windowID=driver.current_window_handle
print(windowID)

windowID_s=driver.window_handles
parWindow=windowID_s[0]
ChildWindow=windowID_s[1]
print(parWindow,ChildWindow)

# driver.switch_to.window(parWindow)
print(driver.title)                      #OrangeHRM
time.sleep(3)
driver.switch_to.window(ChildWindow)      #Human Resources Management Software | OrangeHRM
print(driver.title)
driver.switch_to.window(parWindow)



#Approach2-----------
windowID_s=driver.window_handles

for winid in windowID_s:
    driver.switch_to.window(winid)
    print(driver.title)

#----------Close specific browser windows   1 2 3----------
windowID_s=driver.window_handles

for winid in windowID_s:
    driver.switch_to.window(winid)
    if driver.title=='OrangeHRM':
        driver.close()