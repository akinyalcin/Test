from selenium import webdriver
import time
import unittest
from Data.testdata import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests import loginAccount
from Locators.locators import Locators


class HomepageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:/Hepsiburada/Drivers/chromedriver.exe")
        # cls.driver = webdriver.Firefox(executable_path="E:/Hepsiburada/Drivers/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_homepage(self):

        """
        Homepage test steps:
        1. Check title is correct.
        2. Check header is displayed.
        3. Check different pages on homepage.
        4. Check footer is displayed.
        """

        """ Login Account """
        loginAccount.LoginAccountTest.test_loginAccount(self)

        driver = self.driver
        # Check the homepage title is correct
        self.assertEqual(TestData.homePageTitle, driver.title, "Wrong title!")
        print("Title is correct!")

        # Check the header is displayed on the page
        driver.find_element_by_class_name(Locators.header_class).is_displayed()
        print("Header is displayed!")

        # Check the hero image is displayed and clickable on the page
        driver.find_element_by_class_name(Locators.hero_class).is_displayed()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, Locators.hero_class))
        )
        print("Image is displayed and clickable!")

        # Check different pages on the page

        driver.find_element_by_class_name(Locators.deal_class).is_displayed()
        driver.find_element_by_class_name(Locators.marketing_class).is_displayed()
        driver.find_element_by_class_name(Locators.feature_class).is_displayed()
        driver.find_element_by_class_name(Locators.recommendation_class).is_displayed()
        driver.find_element_by_class_name(Locators.explore_class).is_displayed()
        print("Other pages are displayed!")

        # Check the footer end is displayed
        driver.find_element_by_tag_name("body").send_keys(Keys.END)
        time.sleep(5)
        driver.find_element_by_class_name(Locators.footer_class).is_displayed()
        print("Footer is displayed!")

        print("Homepage is loaded successfully!")

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