import os.path
from asyncio import wait
from fileinput import filename

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #explicit wait
from selenium.webdriver.common.keys import Keys #import keys
import allure

chrome_options = Options() # buitin function
chrome_options.add_argument("--start-maximized")

# for headless and jenkins
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get('https://sauce-demo.myshopify.com/')

time.sleep(5)

# signup page
# signup=wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='seven columns offset-by-one desktop']//a[@id='customer_register_link']")))
# signup.click()
#
# firstname=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first_name']")))
# firstname.send_keys("Swastika")
#
# lastname=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last_name']")))
# lastname.send_keys("Majhi")
#
# email=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='email']")))
# email.send_keys("swastika.gmt3@gmail.com")
#
# password=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']")))
# password.send_keys("Swastika@123")
#
# create=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Create']")))
# create.click()

# login page
# customer_email=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='customer_email']")))
# customer_email.send_keys("swastika.gmt3@gmail.com")
#
# customer_password=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='customer_password']")))
# customer_password.send_keys("Swastika@123")
#
# signin_button=wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Sign In']")))
# signin_button.click()
# driver.execute_script("arguments[0].click();", signin_button)
#
# #wait for dashboard
# home=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='breadcrumb']//a[normalize-space()='Home']")))

# forgot password
# forgot_password=wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Forgot your password?']")))
# # forgot_password.click()
#
# driver.execute_script("arguments[0].click();", forgot_password)
# forgot_password.click()


@allure.step("Take screenshot: {name}")
def  take_screenshot(self,name="screenshot", timestamp=True):
    screenshot_dir="screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    import time
    if timestamp:
        timestamp_str=int(time.time())
        filename= f"{screenshot_dir}/{name}_{timestamp_str}.png"
    else:
        filename=f"{screenshot_dir}/{name}.png"

    self.driver.save_screenshot(filename)

    allure.attach.file(
        filename,
        name=name,
        attachment_type=allure.attachment_type.png
    )
    print(f"Screenshot taken: {filename}")
# function banauney aba individually
#baseclass: assert pani base class,screenshot base class
@allure.step("click on element with xpath: {xpath}")
def click_element(driver,xpath):
    element=driver.find_element(By.XPATH, xpath)
    assert element.is_displayed(), f"element with xpath {xpath} is not displayed"
    element.click()
    take_screenshot(self, name="click_element")
    print(f"Successfully clicked on element: {xpath}")

@allure.step("send keys {keys} to element with xpath: {xpath}")
def send_keys_to_element(driver,xpath,keys):
    element=driver.find_element(By. XPATH, xpath)
    assert element.is_enabled(), f"element with xpath {xpath} is not enabled"
    element.send_keys(keys)
    take_screenshot(driver, name="send_keys")
    print(f"Successfully send keys: {xpath}")


def clear(driver,xpath):
    element=driver.find_element(By. XPATH, xpath)
    element.clear()

#paramaterization of login
Login_search_data= [
    #first test case with email, password, search term
    {
        "email":"swastika.gmt3@gmail.com",
        "password":"Swastika@123",
        "search_term":"product"
    },
    #Second test case
    {
        "email":"testuser2@gmail.com",
        "password":"Password2@",
        "search_term":"shirt"
,   },
    #Third test case
    {
        "email":"testuser3@gmail.com",
        "password":"Password3@",
        "search_term":"hat"
    }
]
# #perform login and search test with the specified credentials
# print("\n performing login and search test..")
# #loop through each test case in our test data
# #enemurate gives us both the index and the data
# #very important line for loop language
# for i, user_data in enumerate(Login_search_data):
#     #navigate back to  the home page for each test
#     driver.get('https://sauce-demo.myshopify.com/account/login')
#     time.sleep(2)
#
#     # find and click the login link
#     login_link="//div[@class='seven columns offset-by-one desktop']//a[@id='customer_login_link']"
#     click_element(driver,login_link)
#     print("clicked on log in link")
#
#     #wait for navigate
#     time.sleep(2)
#
#     #enter email using the  credentials from current test case
#     email_input="//input[@id='customer_email']"
#     send_keys_to_element(driver, email_input, user_data["email"])
#     print(f"Email entered: {user_data['email']}")
#
#     #Enter password
#     password_input="//input[@id='customer_password']"
#     send_keys_to_element(driver, password_input, user_data["password"])
#     print(f"password entered")
#
#     #click sign in button to submit the  login form
#     sigin_in_button="//input[@value='Sign In']"
#     click_element(driver,sigin_in_button)
#     print(f"sign in button clicked")
#
#     time.sleep(200)

search_input="//input[@id='search-field']"
click_element(driver,search_input)
send_keys_to_element(driver,search_input,"grey jacket")
# click_element(driver,search_input)
print(f"product searched")
time.sleep(15)

product1="//img[@alt='Grey jacket']"
click_element(driver,product1)
print(f"product1 searched:")
time.sleep(5)

add_to_cart="//input[@id='add']"
click_element(driver,add_to_cart)
print(f"Add to cart clicked")
time.sleep(5)

checkout="//a[normalize-space()='Check Out']"
click_element(driver,checkout)
print(f"Checkout button clicked")
time.sleep(15)

checkout_button="//input[@id='checkout']"
click_element(driver,checkout_button)
print(f"check out button is clicked")

# For checkout
Email="//input[@id='email']"
send_keys_to_element(driver,Email,"swastika.gmt3@gmail.com")
print(f"Email entered")

time.sleep(5)

# delivery credentials

# # # Click the country dropdown
# driver.find_element(By.XPATH, "//select[@id='Select0']").click()
# # Click Nepal option
# Nepal = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='Nepal']"))
# )
# Nepal.click()
# print("Nepal selected")

First_name="//input[@id='TextField0']"
send_keys_to_element(driver,First_name,"swastika")
print(f"Enter first name")

Last_name="//input[@id='TextField1']"
send_keys_to_element(driver,Last_name,"majhi")
print(f"Enter last name")

Address="//input[@id='TextField3']"
send_keys_to_element(driver,Address,"Sankhamul")
print(f"Enter address")

City="//input[@id='TextField14']"
send_keys_to_element(driver,City,"kathmandu")

time.sleep(5)

Credit_card_number="//div[@class='_9F1Rf GI5Fn _1fragemow _1fragemon _1fragemv4']"
send_keys_to_element(driver,Credit_card_number,"4111 1111 1111 1111")
print(f"credit ccard number entered")





# #navigate to registration page
# signup="//div[@class='seven columns offset-by-one desktop']//a[@id='customer_register_link']"
# click_element(driver,signup)
# print("clicked on sign up link")
#
# #wait for navigate to registration
# time.sleep(2)
#
# #verify registration page open properly by clicking the URL
# if "register" in driver.current_url:
#     print("Registration form loaded successfully")
#     assert True
# else:
#     print("warning: Registration form may not have loaded properly -current URL",driver.current_url)
#     assert False
#
# FirstName="//input[@id='first_name']"
# send_keys_to_element(driver,FirstName,"Swastika")
# print("First name entered")
#
# LastName="//input[@id='last_name']"
# send_keys_to_element(driver, LastName, "Majhi")
# print("Last name entered")
#
# Email="//input[@id='email']"
# #Generate a unique email address each time
# #time.time() comes from python's builtin time module
# #It returns the current time in seconds since jan 1,1978
# #ini(time.time()) converts the floating-point number into an integer
# #f"..." This is an f-string (formatted string). It lets you insert python expression directly
# #testuser_{int(time.time())}@gmail.com" The timestamp is inserted into the email string
#
# unique_email=f"testuser_{int(time.time())}@gmail.com"
# send_keys_to_element(driver,Email,unique_email)
# print("Email entered")
#
# Password="//input[@id='password']"
# send_keys_to_element(driver,Password,"Swastika@123")
# print("password entered")
#
# CreateButton="//input[@value='Create']"
# click_element(driver,CreateButton)
# print("Clicked on create button")
#
# time.sleep(200)
#
# logout_element=driver.find_element((By.XPATH, "//div[@class='seven columns offset-by-one desktop']//a[@id='customer_logout_link']"))
# if logout_element:
#     print("Registration successfull- logout element found successfully")
#     assert True
# else:
#     print("Registration is not successfull- no redirect logout element is not found")
#     assert False
#
# #navigate to login page
# Login="//div[@class='seven columns offset-by-one desktop']//a[@id='customer_login_link']"
# click_element(driver,Login)
# print("click on login link")
#
# Customer_email="//input[@id='customer_email']"
# send_keys_to_element(driver, Customer_email, "swastika.gmt3@gmail.com")
# print("customer email entered")
#
# Customer_Password="//input[@id='customer_password']"
# send_keys_to_element(driver,Customer_Password, "Swastika@123")
# print("Customer password entered")
#
# SignIn_button="//input[@value='Sign In']"
# click_element(driver, SignIn_button)
# print("Signin button clicked")
#
# #Navigate to About us page
# About_Us="//div[@class='seven columns offset-by-one desktop']//a[normalize-space()='About Us']"
# click_element(driver,About_Us)
# prnit("click on About us link")
#
# #Navigate to Search page
# Search="//div[@class='seven columns offset-by-one desktop']//a[normalize-space()='Search']"
# click_element(driver,Search)
# print("click on Search link")

time.sleep(15)



driver.quit()

