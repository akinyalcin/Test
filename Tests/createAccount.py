from selenium import webdriver
import time
import unittest
from Data.testdata import TestData
from Locators.locators import Locators


class CreateAccountTest(unittest.TestCase):

    """
    Create an account test steps:
    1. Open create account url.
    2. Enter account information.
    3. Create an account.
    4. Check the account title is correct.
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:/Hepsiburada/Drivers/chromedriver.exe")
        # cls.driver = webdriver.Firefox(executable_path="E:/Hepsiburada/Drivers/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_createAccount(self):
        print("Create an Account")
        driver = self.driver
        self.signup_url = TestData.signup_url
        if self.signup_url != self.driver.current_url:
            self.driver.get(self.signup_url)
        time.sleep(10)

        driver.find_element_by_xpath(Locators.signupbutton).click()
        self.driver.find_element_by_id(Locators.name_id).clear()
        self.driver.find_element_by_id(Locators.name_id).send_keys(TestData.username)
        self.driver.find_element_by_id(Locators.surname_id).clear()
        self.driver.find_element_by_id(Locators.surname_id).send_keys(TestData.userSurname)
        self.driver.find_element_by_id(Locators.email_id).clear()
        self.driver.find_element_by_id(Locators.email_id).send_keys(TestData.email)
        self.driver.find_element_by_id(Locators.password_id).clear()
        self.driver.find_element_by_id(Locators.password_id).send_keys(TestData.password)
        self.driver.find_element_by_id(Locators.submit_id).click()
        time.sleep(10)
        self.driver.refresh()
        title = self.driver.find_element_by_id(Locators.account_id).text
        print(title)
        self.assertEqual(TestData.myAccountTitle, title, "Title Error!")
        print("The account has been successfully created!")

    @classmethod
    def tearDownClass(cls):
        """
        Terminates the WebDriver test case session.
        """
        cls.driver.close()
        cls.driver.quit()
        print("'Create an Account' Test completed!")


if __name__ == '__main__':
    unittest.main()
