from scoop.shared import elements
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    @allure.step("click on element with xpath: {xpath}")
    def click_element(self,xpath):
        try:
            element=self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            assert element.is_displayed(), f"element with xpath {xpath} is not displayed"
            element.click()
            print(f"Successfully clicked on element: {xpath}")
        except Exception as e: