from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# service_obj = Service("F:\\Python & Selenium by pavan sir\\Drivers\\chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service_obj, options=options)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


driver.maximize_window()
driver.implicitly_wait(10)  # Wait up to 10

driver.get("https://en-gb.facebook.com/")

#1)Csss Selectore ->Tag & ID
# --->Syntax :- Tagname # id Value
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("ABC")
# # -->Note Tagname not mandatory but #with ID Value so #-Hash is mandator for ID
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("ABC")

#2)CSS Selectore ->Tag & Class
# --->Syntax :- Tagname .(DOT) Class Value
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("Part1")
# -->Note Tagname not mandatory but .(DOT)with class Value so.(DOT) is mandator for CLASS
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys(("=part2"))
#3)CSS Selectore ->Tag & Attribute = Value
# --->Syntax :- Tagname[Attribute=Value]
driver.find_element(By.CSS_SELECTOR,"input[placeholder=Password]").send_keys("PWD@2")
# -->Note Tagname not mandatory but [Squre brackets]with Attribute Value so[Squre brackets] is mandator for CLASS
driver.find_element(By.CSS_SELECTOR,"[placeholder=Password]").send_keys("PWD@2")
