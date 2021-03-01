import unittest
import HtmlTestRunner
import  os
from Tests.createAccount import CreateAccountTest
from Tests.loginAccount import LoginAccountTest
from Tests.homepage import HomepageTest
from Tests.addShippingAddress import AddShippingAddress
from Tests.addBillingAddress import AddBillingAddress
from Tests.searchProduct import SearchProduct
from Tests.shoppingCart import ShoppingCart

# get the directory path to output report file
dir = os.getcwd()

# get all tests from Tests
createAccount_test = unittest.TestLoader().loadTestsFromTestCase(CreateAccountTest)
loginAccount_test = unittest.TestLoader().loadTestsFromTestCase(LoginAccountTest)
homepage_test = unittest.TestLoader().loadTestsFromTestCase(HomepageTest)
addShippingAddress_test = unittest.TestLoader().loadTestsFromTestCase(AddShippingAddress)
addBillingAddress_test = unittest.TestLoader().loadTestsFromTestCase(AddBillingAddress)
searchProduct_test = unittest.TestLoader().loadTestsFromTestCase(SearchProduct)
shoppingCart_test = unittest.TestLoader().loadTestsFromTestCase(ShoppingCart)

# create a test suite combining tests
test_suite = unittest.TestSuite([createAccount_test, loginAccount_test, homepage_test, addShippingAddress_test,
                                 addBillingAddress_test, searchProduct_test, shoppingCart_test])

# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HtmlTestRunner.HTMLTestRunner(stream=outfile, report_title="Test Report")

# run the suite using HtmlTestRunner
runner.run(test_suite)