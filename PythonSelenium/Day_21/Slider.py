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

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
min_Slider_Length=driver.find_element(By.XPATH,"//span[1]")
max_Slider_Length=driver.find_element(By.XPATH,"//span[2]")

print("Location of sliders Before moving........")
print(min_Slider_Length.location)            #{'x': 59, 'y': 250}
print(max_Slider_Length.location)            #{'x': 510, 'y': 250}

act=ActionChains(driver)

act.drag_and_drop_by_offset(min_Slider_Length,100,0).perform()
act.drag_and_drop_by_offset(max_Slider_Length,-120,0).perform()
