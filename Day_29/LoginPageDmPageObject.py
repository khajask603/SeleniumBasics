from selenium import webdriver
from selenium.webdriver.common.by import By


class AccountLogin:

# ------------Locatores----------
    txtbox_loginEmail_Xpath="//input[@id='input-email']"
    txtbox_loginPassword_Xpath ="//input[@id='input-password']"
    loginButton_Xpath = "//input[@value='Login']"


# ------------Constructore----------
    def __init__(self, driver):
        self.driver=driver

# ------------Action methods----------

#        txtbox_loginEmail_Xpath="//input[@id='input-email']"l']"
    def sendEmail(self, emailAdress):
        loginemailTXT = self.driver.find_element(By.XPATH, self.txtbox_loginEmail_Xpath)
        loginemailTXT.send_keys(emailAdress)

        # txtbox_loginPassword_Xpath = "//input[@id='input-password']"
    def sendPasword(self, pasword):
        loginpaswordTXT = self.driver.find_element(By.XPATH, self.txtbox_loginPassword_Xpath)
        loginpaswordTXT.send_keys(pasword)


        # loginButton_Xpath = "//input[@value='Login']"
    def Login_Button(self):
        loginButton = self.driver.find_element(By.XPATH, self.loginButton_Xpath)
        loginButton.click()

