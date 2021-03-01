from selenium import webdriver
import time
import unittest
from Data.testdata import TestData
from Locators.locators import Locators
from selenium.webdriver.common.keys import Keys


class LoginAccountTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:/Hepsiburada/Drivers/chromedriver.exe")
        # cls.driver = webdriver.Firefox(executable_path="E:/Hepsiburada/Drivers/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_loginAccount(self):

        """
        Login account test steps:
        1. Open login url.
        2. Enter wrong login information.
        3. Check the error message is displayed.
        4. Enter correct login information.
        5. Check the account title is correct.
        """

        print("Login Account")

        self.login_url = TestData.login_url
        if self.login_url != self.driver.current_url:
            self.driver.get(self.login_url)
        time.sleep(10)

        self.driver.find_element_by_id(Locators.username_id).clear()
        self.driver.find_element_by_id(Locators.username_id).send_keys(TestData.email)
        self.driver.find_element_by_id(Locators.userpass_id).clear()
        self.driver.find_element_by_id(Locators.userpass_id).send_keys(TestData.wrong_password)
        self.driver.find_element_by_id(Locators.loginbtn).click()
        self.driver.find_element_by_xpath(Locators.errmsg_path).is_displayed()
        print("Wrong username or password. Login failed!")
        self.driver.find_element_by_id(Locators.username_id).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element_by_id(Locators.username_id).send_keys(TestData.email)
        self.driver.find_element_by_id(Locators.userpass_id).send_keys(Keys.CONTROL, 'a')
        self.driver.find_element_by_id(Locators.userpass_id).send_keys(TestData.password)
        self.driver.find_element_by_id(Locators.loginbtn).click()
        time.sleep(10)
        self.driver.refresh()
        title = self.driver.find_element_by_id(Locators.account_id).text
        print(title)
        self.assertEqual(TestData.myAccountTitle, title, "Title Error!")
        print("The account has been logged in successfully!")

    @classmethod
    def tearDownClass(cls):
        """
        Terminates the WebDriver test case session.
        """
        cls.driver.close()
        cls.driver.quit()
        print("'Login Account' Test completed!")


if __name__ == '__main__':
    unittest.main()
