import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from LoginPageDmPageObject import AccountLogin
from RegisterPageObject import AccountRegister


class Test_Register_Login:

    def test_register_success(self,setup):
        self.driver=setup
        register_page = AccountRegister(self.driver)
        self.driver.get("https://naveenautomationlabs.com/opencart/index.php?route=account/register")
        register_page.setFirstName("Shaik")
        register_page.setLastName("khajaMohiddin")
        register_page.setEmail("khajask503@gmail.com")
        register_page.setTelephone("8143264121")
        register_page.setpassword("WHite@456")
        register_page.setConfirm_password("WHite@456")
        register_page.clickNews_RadioButton()
        register_page.click_policy_Button()
        register_page.continue_Button()

        alert_locator = register_page.get_alert_locator()
        alert_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(alert_locator))
        alert_text = alert_element.text
        print(alert_text)

    def test_login(self,setup):
        self.driver=setup
        self.driver.get("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
        login_page = AccountLogin(self.driver)
        login_page.sendEmail("khajask503@gmail.com")
        login_page.sendPasword("White@456")
        login_page.Login_Button()


