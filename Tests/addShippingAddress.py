from selenium import webdriver
import time
import unittest
from Data.testdata import TestData
from Tests import loginAccount
from Locators.locators import Locators


class AddShippingAddress(unittest.TestCase):

    """
     1. Navigate Address page.
     2. Add a new Shipping Address.
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:/Hepsiburada/Drivers/chromedriver.exe")
        # cls.driver = webdriver.Firefox(executable_path="E:/Hepsiburada/Drivers/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_ShippingAddress(self):

        """ Login Account """
        loginAccount.LoginAccountTest.test_loginAccount(self)
        driver = self.driver

        self.driver.get(TestData.account_url)
        time.sleep(5)
        driver.refresh()
        driver.find_element_by_xpath(Locators.shipping_path).click()
        driver.find_element_by_xpath(Locators.newaddress_path).click()
        driver.find_element_by_name(Locators.firstname_name).send_keys(TestData.username)
        driver.find_element_by_name(Locators.lastname_name).send_keys(TestData.userSurname)
        driver.find_element_by_xpath(Locators.country_path).click()
        driver.find_element_by_xpath(Locators.city1_path).click()
        driver.find_element_by_xpath(Locators.city2_path).click()
        driver.find_element_by_xpath(Locators.city3_path).click()
        driver.find_element_by_name(Locators.addressline_name).send_keys(TestData.addressLine)
        driver.find_element_by_name(Locators.addressname_name).send_keys(TestData.addressName)
        driver.find_element_by_name(Locators.phone_name).send_keys(TestData.phone)
        driver.find_element_by_xpath(Locators.save_shipping).click()
        time.sleep(5)
        addressname = driver.find_element_by_xpath(Locators.created_addressname_path).text
        self.assertEqual(TestData.addressName, addressname, "Address Error!")
        print("Shipping address is created!")


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