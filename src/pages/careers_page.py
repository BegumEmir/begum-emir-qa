from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CareersPage:
    def __init__(self, driver):
        self.driver = driver
        self.LOCATIONS_BLOCK= (By.XPATH, "//h3[normalize-space(text() =  'Our Locations')]")
        self.TEAMS_BLOCK = (By.XPATH, "//a[text() = 'See all teams']")
        self.LIFE_AT_INSIDER_BLOCK = (By.XPATH, "//h2[text() = 'Life at Insider']")

    def is_loaded(self):
        return "Careers" in self.driver.title

    def are_blocks_visible(self):
        
        return all([
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOCATIONS_BLOCK)).is_displayed(),
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TEAMS_BLOCK)).is_displayed(),
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LIFE_AT_INSIDER_BLOCK)).is_displayed(),
        ])
