from selenium import webdriver
import time
import unittest
from Data.testdata import TestData
from Tests import loginAccount
from Locators.locators import Locators


class SearchProduct(unittest.TestCase):

    """
    Search test steps:
    1. Search according to the product.
    2. Check how many products are displayed on the page.
    3. Check the results are releated to the search product.
    4. Get the product details.
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:/Hepsiburada/Drivers/chromedriver.exe")
        # cls.driver = webdriver.Firefox(executable_path="E:/Hepsiburada/Drivers/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_searchProduct(self):

        loginAccount.LoginAccountTest.test_loginAccount(self)

        driver = self.driver
        driver.find_element_by_class_name("logo-hepsiburada").click()
        time.sleep(5)

        ### Check search field according to product ###

        print("Check search field according to product:")
        driver.find_element_by_class_name(Locators.search_field_name).send_keys(TestData.searchProduct)
        driver.find_element_by_class_name(Locators.search_button_name).click()
        time.sleep(5)
        keyword = driver.find_element_by_xpath(Locators.keyword_path).text
        self.assertEqual(keyword, TestData.searchProduct, "Keywords are not matched!")

        # Check how many products are shown on the first page
        results = driver.find_elements_by_class_name(Locators.product_detail_name)
        print(len(results), "products are shown on the first page!")

        # Check the results are related to the search text
        for i in range(len(results)):
            self.assertIn(TestData.searchProduct, results[i].text, "Product info does not contain the search text!")
        print("All products are related to the search!")

        results[0].click()
        time.sleep(5)
        productname = driver.find_element_by_id(Locators.prodname_name).text
        print("Product Name: ", productname)
        originalprice = driver.find_element_by_id(Locators.orgprice_id).text
        print("Original Price: ", originalprice)
        offeringprice = driver.find_element_by_id(Locators.ofrprice_id).text
        print("Product Price: ", offeringprice)
        productdiscount = driver.find_element_by_xpath(Locators.discount_path).text
        print("Product Discount: %", productdiscount)
        productseller = driver.find_element_by_xpath(Locators.seller_path).text
        print("Product Seller: ", productseller)

        rating = driver.find_element_by_class_name(Locators.rating_name).text
        print("Rating: ", rating)

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