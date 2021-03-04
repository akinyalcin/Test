
class Locators():

    """ Create Account Page Objects """
    signupbutton = "//*[@id='root']/div/div/div[2]/div/div/div[2]/div[1]/div[2]"
    name_id = "txtName"
    surname_id = "txtSurname"
    email_id = "txtEmail"
    password_id = "txtNewPassEmail"
    submit_id = "btnSignUpSubmit"
    account_id = "myAccount"

    """ Login Account Page Objects """
    username_id = "txtUserName"
    userpass_id = "txtPassword"
    loginbtn = "btnLogin"
    errmsg_path = "/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[2]"
    logout_path = "//*[@id='myAccount']/div/div[2]/ul/li[9]/a"
    different_account_path = "//*[@id='root']/div/div/div[2]/div/div/div/div[4]/div"
    continuewithoutlogin_path = "//*[@id='root']/div/div/div[2]/div/div/div/div[2]/div/div[1]"
    btnWithoutMembership_id = "btnWithoutMemberShip"

    """ Homepage Objects """
    header_class = "sf-OldHeader-5sPZX"
    hero_class = "sf-HerouselBaseTemplate-140fN"
    deal_class = "sf-DealOfTheDay-3mP0O"
    marketing_class = "sf-MarketingBillboard-1UkbC"
    feature_class = "sf-FeatureList-3R48W"
    recommendation_class = "sf-Recommendation-aOWMV"
    explore_class = "sf-Explore-1pWGu"
    footer_class = "footer-end"

    """ Address Page Objects """
    address_path = "//*[@id='AccountMenu']/div/div/div[2]/div/div[7]/a/div[2]"
    shipping_path = "//*[@id='AccountMenu']/div/div/div[2]/div/div[7]/a/div[2]"
    billing_path = "//*[@id='customer-addresses']/div/ul/li[2]/a"
    newaddress_path = "//*[@id='customer-addresses']/div/div/div/ul/li/a"
    firstname_name = "firstName"
    lastname_name = "lastName"
    country_path = "//*[@id='form-address']/div/div/section[2]/div[3]/div/div/button/span[2]"
    city1_path = "//*[@id='form-address']/div/div/section[2]/div[3]/div/div/div/ul/li[4]/a/span"
    city2_path = "//*[@id='form-address']/div/div/section[2]/div[4]/div/div/button/span[2]"
    city3_path = "//*[@id='form-address']/div/div/section[2]/div[4]/div/div/div/ul/li[5]/a/span"
    addressline_name = "address"
    addressname_name = "addressName"
    phone_name = "phone"
    phone_name2 = "phoneNumber.gsmNumber"
    save_shipping = "//*[@id='form-address']/div/div/div[2]/div/button"
    save_billing = "//*[@id='form-address']/div/div/div[4]/div/button"
    created_addressname_path = "//*[@id='customer-addresses']/div/div/div/ul/li[2]/div/h4/span"


    """ Search Product Page Objects """
    search_field_name = "desktopOldAutosuggestTheme-input"
    search_button_name = "SearchBoxOld-buttonContainer"
    keyword_path = "//*[@id='categorySuggestionList']/div[1]/h1"
    product_detail_name = "product-detail"
    prodname_name = "product-name"
    orgprice_id = "originalPrice"
    ofrprice_id = "offering-price"
    discount_path = "//*[@id='product-discount-rate']/span/span"
    seller_path = "/html/body/div[2]/main/div[3]/section[1]/div[5]/div/div[4]/div[1]/div[2]/div/div[1]/div[5]/" \
                  "div/span/span[2]/a"
    rating_name = "rating-star"


    """ Shopping Card Page Objects """
    add_first_cart_name = "addToCart"
    add_second_cart_path = "/html/body/div[2]/main/div[3]/section[1]/div[5]/div/div[4]/div[2]/div[2]/div/" \
                           "div[2]/table/tbody/tr[2]/td[3]/div/form/button"
    productname_class = "product_name_3Lh3t"
    productprice_class = "product_priceBox_3V_jx"
    totalprice_class = "total_price_3V-CM"
    continuestepbtn = "continue_step_btn"
    shippingselection = "//*[@id='shipping']/div/div[1]/div[1]/div[1]/label/input"
    paymentmethod_path = "//*[@id='payment-methods']/div/div[1]/div[1]/div[1]/label/input"
    cardnumber_name = "cardNumber"
    holdername_name = "holderName"
    expiredate_name = "expireDate"
    cvv_name = "cvv"
    carderrmsg_path = "//*[@id='payment-methods']/div[1]/div/div[2]/div/div[1]/form/div[1]/div[1]/div/div/span"


    """ Address on the Shopping Cart Page Objects"""

    city11_path = "//*[@id='app']/div/div/div[1]/div/div[1]/div[2]/div/" \
                  "div[2]/div/form/fieldset[2]/div/div[1]/div/div[1]/div/input"

    city12_path = "/html/body/div/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/form/" \
                  "fieldset[2]/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[1]"

    city21_path = "//*[@id='app']/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/form/" \
                  "fieldset[2]/div/div[1]/div/div[2]/div/input"

    city22_path = "/html/body/div/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/form/" \
                  "fieldset[2]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[3]"

    city31_path = "//*[@id='app']/div/div/div[1]/div/div[1]/div[2]/div/" \
                  "div[2]/div/form/fieldset[2]/div/div[1]/div/div[3]/div/input"

    city32_path = "/html/body/div/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/form/" \
                  "fieldset[2]/div/div[1]/div/div[3]/div/div[2]/div/div[2]/div/div[4]"
