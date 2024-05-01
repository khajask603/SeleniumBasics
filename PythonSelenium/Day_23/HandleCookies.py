from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj=Service(r"F:\Python & Selenium by pavan sir\Drivers\chromedriver.exe")
ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj, options=ops)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")

#Capture Cookies from the browser
cookies=driver.get_cookies()

#Capture Cookies from the browser
cookies=driver.get_cookies()
print("Size of cookies:",len(cookies)) #3

#Print details of all cookies
for ck in cookies:
     # print(ck)                          #Pritn All the cokkies of thwe website
     print(ck.get('name'),":",ck.get('value'))

#Add new cookie to the browser
driver.add_cookie({"name":"My Cokkie", "value":"1234567"})
cookies=driver.get_cookies()
print("Size of cookies after adding new one:",len(cookies)) #4

#Delete specific cookie from the browser
driver.delete_cookie("My Cokkie")
cookies=driver.get_cookies()
print("Size of cookies after Deleting new one:",len(cookies)) #3

#Delete all the cookies

driver.delete_all_cookies()
cookies=driver.get_cookies()
print("Size of cookies after Deleting new one:",len(cookies)) #0