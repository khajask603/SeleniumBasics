from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
# Requiremnt
# 1) Count number of rows & columns
# 2) Read specific row & Column data
# 3) Read all the rows & Columns data
# 4) Read data based on condition(List books name whose author is Mukesh)

driver.get("https://testautomationpractice.blogspot.com/")
noOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(noOfRows)          #---->7
noOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]//th"))
print(noOfColumns)       #--->4

# 2) Read specific row & Column data
# Ex:- 5th row 1st column
data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]//td[1]").text
print(data)     #Master In Selenium

# 3) Read all the rows & Columns data
print("printing all the rows and columns data.....................")

# for row in range(2,noOfRows+1):
#     for Col in range(1,noOfColumns+1):
#         data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(row)+"]//td["+str(Col)+"]").text
#         print(data,end='                        ')
#     print()

# 4) Read data based on condition(List books name whose author is Mukesh)
for row in range(2,noOfRows+1):
    authorName=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(row)+"]//td[2]").text
    if authorName=='Mukesh':
        BookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]//td[1]").text
        Price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]//td[4]").text
        print(BookName ,", Authore :- ",authorName, "Price ",Price)

