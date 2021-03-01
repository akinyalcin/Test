from selenium import webdriver
import time
import unittest
from Data.testdata import TestData
from Tests import searchProduct
from Locators.locators import Locators


class ShoppingCart(unittest.TestCase):

    """
    Shopping Cart test steps:
    1. Search product.
    2. Select the first product from the results.
    3. Add the product to the cart.
    4. Add the product to the cart from another seller.
    5. Check the product names are correct in the cart.
    6. Check the total product prices are correct in the cart.
    7. Select the shipping address.
    8. Select credit card as a payment type.
    9. Enter wrong credit card informations.
    10. Check the error message.
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:/Hepsiburada/Drivers/chromedriver.exe")
        # cls.driver = webdriver.Firefox(executable_path="E:/Hepsiburada/Drivers/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_shoppingCart(self):

        searchProduct.SearchProduct.test_searchProduct(self)

        driver = self.driver

        driver.find_element_by_id(Locators.add_first_cart_name).click()
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath(Locators.add_second_cart_path).click()
        time.sleep(5)
        driver.refresh()
        time.sleep(10)

        driver.get(TestData.shoping_cart_url)
        time.sleep(5)

        productname = driver.find_elements_by_class_name(Locators.productname_class)
        product1 = productname[0].text
        product2 = productname[1].text
        print(product1)
        print(product2)

        """ 
        #Case: There is a bonus product #

        product1 = productname[0].text
        product2 = productname[1].text
        product3 = productname[2].text
        print(product1)
        print(product2)
        print(product3)

        """

        self.assertEqual(product1, TestData.productname, "Product Error!")
        self.assertEqual(product2, TestData.gift, "Product Error!")
        #self.assertEqual(product3, TestData.productname, "Product Error!")

        print("Product is added to the cart!")

        price = driver.find_elements_by_class_name(Locators.productprice_class)
        price1 = price[0].text
        price2 = price[1].text
        prices = [price1, price2]

        newprices = [i[:-3] for i in prices]
        newprices = [i.replace(",", ".") for i in newprices]
        newprices = [float(i) for i in newprices]

        total = sum(newprices)
        lastprice = str(total) + " TL"
        lastprice = lastprice.replace(".", ",")
        print("Last Price: ", lastprice)

        totalprice = driver.find_element_by_class_name(Locators.totalprice_class).text
        totalprice = totalprice.replace("\n", " ")
        print("Total Price: ", totalprice)

        self.assertEqual(lastprice, totalprice, "Price and Total Price are not equal!")

        time.sleep(5)
        driver.find_element_by_id(Locators.continuestepbtn).click()
        time.sleep(5)

        driver.find_element_by_xpath(Locators.shippingselection).click()
        driver.find_element_by_id(Locators.continuestepbtn).click()
        time.sleep(5)
        driver.find_element_by_xpath(Locators.paymentmethod_path).click()
        driver.find_element_by_name(Locators.cardnumber_name).send_keys(TestData.cardNumber)
        driver.find_element_by_name(Locators.holdername_name).send_keys(TestData.holderName)
        driver.find_element_by_name(Locators.expiredate_name).send_keys(TestData.expireDate)
        driver.find_element_by_name(Locators.cvv_name).send_keys(TestData.cvv)

        invalidcardtext = driver.find_element_by_xpath(Locators.carderrmsg_path).text
        self.assertEqual(invalidcardtext, TestData.invalidCard, "Invalid Card Message Error!")
        print("Payment error because of invalid card data!")
        print("Test completed successfully!")

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
