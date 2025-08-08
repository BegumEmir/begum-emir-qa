from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.COMPANY_MENU = (By.XPATH, "//a[normalize-space()='Company']")
        self.CAREERS_LINK = (By.XPATH, "//a[normalize-space()='Careers']")

    def open(self):
        self.driver.get("https://useinsider.com/")

    def is_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains("Insider"))
        return "Insider" in self.driver.title
    
    def navigate_to_careers(self):
        actions = ActionChains(self.driver)
        company_element = self.driver.find_element(*self.COMPANY_MENU)
        actions.move_to_element(company_element).perform()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*self.CAREERS_LINK))  