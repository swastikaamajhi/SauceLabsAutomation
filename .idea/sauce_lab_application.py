from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #explicit wait
from selenium.webdriver.common.keys import Keys #import keys

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://accounts.saucelabs.com/am/XUI/#login/')

time.sleep(5)

