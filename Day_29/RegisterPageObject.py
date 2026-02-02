from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountRegister:

#------------Locatores----------
    txtbox_FirstName_ID="input-firstname"
    txtbox_LastName_CSSID="#input-lastname"
    txtbox_Email_Xpath="//input[@id='input-email']"
    txtbox_Telephone_Xpath="//input[@id='input-telephone']"
    txtbox_Pasword_ID="input-password"
    txtbox_Confirm_Pasword_ID = "input-confirm"
    NewsLeter_Radio_Button_Xpath="(//label/input[@type='radio'])[2]"
    policy_CheckBox_Xpath="//input[@name='agree']"
    continue_Button_Xpath="//input[@value='Continue']"

# ------------Constructore----------
    def __init__(self, driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)


# ------------Action methods----------
    def setFirstName(self,firstName):
        fnTXT=self.driver.find_element(By.ID, self.txtbox_FirstName_ID)
        fnTXT.send_keys(firstName)

    def setLastName(self,LastName):
        lnText=self.driver.find_element(By.CSS_SELECTOR,self.txtbox_LastName_CSSID)
        lnText.send_keys(LastName)

#    txtbox_Email_Xpath="//input[@id='input-email']"
    def setEmail(self,Email):
        emailTXT=self.driver.find_element(By.XPATH,self.txtbox_Email_Xpath)
        emailTXT.send_keys(Email)

 #   txtbox_Telephone_Xpath="//input[@id='input-telephone']"
    def setTelephone(self, mobile):
        numberTXT = self.driver.find_element(By.XPATH, self.txtbox_Telephone_Xpath)
        numberTXT.send_keys(mobile)

#    txtbox_Pasword_ID="input-password"
    def setpassword(self, pasword):
        paswrdTXT = self.driver.find_element(By.ID, self.txtbox_Pasword_ID)
        paswrdTXT.send_keys(pasword)

#       txtbox_Confirm_Pasword_ID = "input-confirm"
    def setConfirm_password(self, cnfpasword):
        cnfPaswrdTXT = self.driver.find_element(By.ID, self.txtbox_Confirm_Pasword_ID)
        cnfPaswrdTXT.send_keys(cnfpasword)

#    NewsLeter_Radio_Button_Xpath="(//label/input[@type='radio'])[2]"
    def clickNews_RadioButton(self):
        cnfPaswrdTXT = self.driver.find_element(By.XPATH, self.NewsLeter_Radio_Button_Xpath)
        cnfPaswrdTXT.click()

    #    policy_CheckBox_Xpath="//input[@name='agree']"
    def click_policy_Button(self):
        pCButton=self.driver.find_element(By.XPATH,self.policy_CheckBox_Xpath)
        pCButton.click()
#    continue_Button_className="btn-primary"
    def continue_Button(self):
        ConButton=self.driver.find_element(By.XPATH,self.continue_Button_Xpath)
        ConButton.click()
    def get_alert_locator(self):
        """
        Returns the locator for the alert element with class 'alert-danger'.
        """
        return By.CLASS_NAME, "alert-danger"







