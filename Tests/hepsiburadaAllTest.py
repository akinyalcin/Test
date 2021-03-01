import unittest
from selenium import webdriver
import time
from Data.testdata import TestData
from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HepsiburadaAllTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="E:/Hepsiburada/Drivers/chromedriver.exe")
        # cls.driver = webdriver.Firefox(executable_path="E:/Hepsiburada/Drivers/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_createAccount(self):

        """
        Create an account test steps:
        1. Open create account url.
        2. Enter account informations.
        3. Create an account.
        4. Check the account title is correct.
        """

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
        self.assertEqual(TestData.myAccountTitle, title, "Titles did not match!")
        print("The account has been successfully created!")

    def test_02_loginAccount(self):

        """
        Login account test steps:
        1. Open login url.
        2. Enter wrong login informations.
        3. Check the error message is displayed.
        4. Enter correct login informations.
        5. Check the account title is correct.
        """

        print("Login Account")

        self.login_url = TestData.login_url
        if self.login_url != self.driver.current_url:
            self.driver.get(self.login_url)
        time.sleep(10)

        self.driver.find_element_by_xpath(Locators.different_account_path).click()
        time.sleep(5)

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
        self.assertEqual(TestData.myAccountTitle, title, "Titles did not match!")
        print("The account has been logged in successfully!")

    def test_03_homepage(self):

        """
        Homepage test steps:
        1. Check title is correct.
        2. Check header is displayed.
        3. Check different pages on homepage.
        4. Check footer is displayed.
        """

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


    def test_04_ShippingAddress(self):

        """
         1. Navigate Address page.
         2. Add a new Shipping Address.
        """

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


    def test_05_BillingAddress(self):

        """
        1. Navigate Address page.
        2. Add a new Billing Address.
        """
        driver = self.driver

        self.driver.get(TestData.account_url)
        time.sleep(5)
        self.driver.refresh()
        driver.find_element_by_xpath(Locators.address_path).click()
        driver.find_element_by_xpath(Locators.billing_path).click()
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
        driver.find_element_by_xpath(Locators.save_billing).click()
        time.sleep(5)
        addressname = driver.find_element_by_xpath(Locators.created_addressname_path).text
        self.assertEqual(TestData.addressName, addressname, "Address Error!")
        print("Billing address is created!")


    def test_06_searchProduct(self):

        """
        Search test steps:
        1. Search according to the product.
        2. Check how many products are displayed on the page.
        3. Check the results are releated to the search product.
        4. Get the product details.
        """

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


    def test_07_shoppingCart(self):

        """
        Shopping Cart test steps:
        1. Search brand.
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
        print("'Create an Account' Test completed!")


if __name__ == '__main__':
    unittest.main()