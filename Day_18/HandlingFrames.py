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
driver.get("https://chercher.tech/practice/frames")

#-->Frame 1
driver.switch_to.frame("iamframe")                                      #-->Using Name
frame1=driver.find_element(By.XPATH,"//input[@type='text']")
frame1.send_keys("Automation")

#-->Frame 3
driver.switch_to.frame("frame3")                                         #-->Using ID
frame3=driver.find_element(By.XPATH,"//body/b").text
print(frame3)
cb=driver.find_element(By.XPATH,"//input[@id='a']").click()
driver.switch_to.parent_frame()
driver.switch_to.default_content()

#--> Frame->2
frame2 = driver.find_element(By.XPATH, "//iframe[@id='frame2']")         #-->Using WebElement.
driver.switch_to.frame("frame2")
# dd=driver.find_element(By.ID,"animals").click()
dd=driver.find_element(By.ID,"animals")
ddList=Select(dd)
ddList.select_by_visible_text("Avatar")
driver.switch_to.default_content()

# --------------------------------------------------------------------------
# -Frames/Iframes-->Notes-----
# -------------
# switch_to_frame()   # selenium3
# #selenium4
# switch_to.frame(name of the frame)
# switch_to.frame(id of the frame)
# switch_to.frame(webelement)
# switch_to.frame(0)
#
# driver.switch_to.default_content()  ->To Navigate to top Ansestore from any frame
# driver.switch_to.parent_frame()-->To Navigate to Imediate Parent
# frame
# iframe
# form