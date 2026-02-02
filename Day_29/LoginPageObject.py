from selenium import webdriver
from selenium.webdriver.common.by import By
class loginPage:

#------------Locatores----------
    txtbox_UserName_Id="Email"
    txtbox_UserPasword_Id = "Password"
    button_Login_Xpath="//button[@type='submit']"

#------------Constructore----------
    def __init__(self,driver):
        self.driver=driver

#------------Action methods----------
    def setUserName(self, userName):
        usernameTxt = self.driver.find_element(By.ID, self.txtbox_UserName_Id)
        usernameTxt.clear()
        usernameTxt.send_keys(userName)

    def setUserPasword(self, pasword):
        paswordText=self.driver.find_element(By.ID,self.txtbox_UserPasword_Id)
        paswordText.clear()
        paswordText.send_keys(pasword)

    def click_Login_Button(self):
        loginButton = self.driver.find_element(By.XPATH, self.button_Login_Xpath)
        loginButton.click()
