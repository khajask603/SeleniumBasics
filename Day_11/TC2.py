from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)  # Wait up to 10 seconds

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()