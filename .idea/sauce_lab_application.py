from asyncio import wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #explicit wait
from selenium.webdriver.common.keys import Keys #import keys

chrome_options = Options() # buitin function
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get('https://sauce-demo.myshopify.com/account/login')

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

# function banauney aba individually

def click_element(driver,xpath):
    element=driver.find_element(By.XPATH, xpath)
    element.click()

def send_keys_to_element(driver,xpath,keys):
    element=driver.find_element(By. XPATH, xpath)
    element.send_keys(keys)

def clear(driver,xpath):
    element=driver.find_element(By. XPATH, xpath)
    element.clear()

#navigate to registration page
signup="//div[@class='seven columns offset-by-one desktop']//a[@id='customer_register_link']"
click_element(driver,signup)
print("clicked on sign up link")

#wait for navigate to registration
time.sleep(2)

#verify registration page open properly by clicking the URL
if "register" in driver.current_url:
    print("Registration form loaded successfully")
    assert True
else:
    print("warning: Registration form may not have loaded properly -current URL",driver.current_url)
    assert False

FirstName="//input[@id='first_name']"
send_keys_to_element(driver,FirstName,"Swastika")
print("First name entered")

LastName="//input[@id='last_name']"
send_keys_to_element(driver, LastName, "Majhi")
print("Last name entered")

Email="//input[@id='email']"
#Generate a unique email address each time
#time.time() comes from python's builtin time module
#It returns the current time in seconds since jan 1,1978
#ini(time.time()) converts the floating-point number into an integer
#f"..." This is an f-string (formatted string). It lets you insert python expression directly
#testuser_{int(time.time())}@gmail.com" The timestamp is inserted into the email string

unique_email=f"testuser_{int(time.time())}@gmail.com"
send_keys_to_element(driver,Email,unique_email)
print("Email entered")

Password="//input[@id='password']"
send_keys_to_element(driver,Password,"Swastika@123")
print("password entered")

CreateButton="//input[@value='Create']"
click_element(driver,CreateButton)
print("Clicked on create button")

time.sleep(15)
driver.quit()