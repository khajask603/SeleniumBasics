from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
ip1=driver.find_element(By.CSS_SELECTOR,"#inputText1").send_keys("Welcome to Selenium")
ip2=driver.find_element(By.CSS_SELECTOR,"#inputText2")
#Action Classs------------Decleration
act=ActionChains(driver)

#Step-1 -->Ctrl+A  Select the text
# A)Steps
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.UP)
act.perform()
# B)Sending above steps in single Line
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#Step-2 -->#Giving input1  --->Ctrl+C  Copy text
# A)Steps
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()
# B)Sending above steps in single Line
# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#Step-3 -->#Press Tab key to navigate to input2( second)
# A)Steps
act.send_keys(Keys.TAB)
act.perform()
# B)Sending above steps in single Line
# act.send_keys(Keys.TAB).perform()

#Step-4 -->Ctrl+V Past the text
# A)Steps
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()
# B)Sending above steps in single Line
# act.key_up(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()