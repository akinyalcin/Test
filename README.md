# Test Automation for www.hepsiburada.com Website

**Drivers:**

* chromedriver.exe
* geckodriver.exe

**Data:**

* testdata.py : Includes test data which are used in the test automation scripts.

**Locators:**

* locators.py: Includes locators which are used in the test automation scripts.

**Tests:**

* createAccount.py      : Create an Account Test Script
* loginAccount.py       : Login Account Test Script
* homepage.py           : Homepage Test Script
* addShippingAddress.py : Shipping Address Adding Test Script
* addBillingAddress.py  : Billing Address Adding Test Script
* searchProduct.py      : Prduct Search Test Script
* shoppingCart.py       : Shopping Cart Test Script

* hepsiburadaAllTest.py : End to End Test from Create an Account to Shopping Cart
* hepsiburadaAllHtml.py : End to End Test with HtmlTestRunner and Report from Create an Account to Shopping Cart

* hepsiburadaAllWithoutLogin.py     : End to End Test for Homepage - Search Product - Shopping Cart without Login
* hepsiburadaAllWithoutLoginHtml.py : End to End Test with HtmlTestRunner and Report for Homepage - Search Product - Shopping Cart without Login

* hepsiburadaHtml.py : All Tests Seperately in One Test Suit with HtmlTestRunner and Report

**TestCases.xlsx :** Functional Manual Login Test Cases with Steps and Expected Results
