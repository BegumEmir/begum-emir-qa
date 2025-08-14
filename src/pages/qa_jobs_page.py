from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class QAJobsPage:
    URL = "https://useinsider.com/careers/quality-assurance/"

    SEE_ALL_QA      = (By.XPATH, "//a[contains(normalize-space(.),'See all QA jobs')]")
    DEPARTMENT_BOX  = (By.CSS_SELECTOR, "#select2-filter-by-department-container")
    LOCATION_BOX    = (By.CSS_SELECTOR, "#select2-filter-by-location-container")
    RESULTS_LIST    = (By.CSS_SELECTOR, ".select2-results__options")

    ISTANBUL_OPT = (
        By.XPATH,
        "//li[contains(@class,'select2-results__option')]"
        "[contains(.,'Istanbul') and (contains(.,'Turkey') or contains(.,'Türkiye') or contains(.,'Turkiye'))]"
    )

    TITLE_NODES = (By.CSS_SELECTOR, "p.position-title")

    _COOKIE_TRY = [
        (By.ID, "wt-cli-accept-all-btn"),
        (By.XPATH, "//*[self::button or self::a][contains(.,'Accept All') or contains(.,'Kabul') or contains(.,'Tümünü kabul')]"),
    ]

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)
        self._accept_cookies_if_present()

    def _accept_cookies_if_present(self):
        for loc in self._COOKIE_TRY:
            try:
                self.wait.until(EC.element_to_be_clickable(loc)).click()
                return
            except Exception:
                pass

    
    def _wait_department_is_qa(self):
        self.wait.until(EC.url_contains("department=qualityassurance"))
        self.wait.until(EC.text_to_be_present_in_element(self.DEPARTMENT_BOX, "Quality Assurance"))

    def click_see_all_qa(self):
        self.wait.until(EC.element_to_be_clickable(self.SEE_ALL_QA)).click()
        self.wait.until(EC.url_contains("/careers/open-positions"))
        self._wait_department_is_qa()
        self.wait.until(EC.visibility_of_element_located(self.LOCATION_BOX))

    def filter_location_istanbul(self):
        
        self._wait_department_is_qa()

        box = self.wait.until(EC.element_to_be_clickable(self.LOCATION_BOX))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", box)

        
        for attempt in range(2):
            box.click()
            self.wait.until(EC.presence_of_element_located(self.RESULTS_LIST))
            try:
                opt = self.wait.until(EC.presence_of_element_located(self.ISTANBUL_OPT))
                
                try:
                    self.wait.until(EC.element_to_be_clickable(self.ISTANBUL_OPT))
                    opt.click()
                except Exception:
                    
                    self.driver.execute_script("arguments[0].click();", opt)
                break
            except TimeoutException:
                if attempt == 1:
                    raise  
                
                continue

        
        self.wait.until(lambda d: "istanbul" in (d.find_element(*self.LOCATION_BOX).text or "").lower())
        self.wait.until(EC.presence_of_all_elements_located(self.TITLE_NODES))

    def has_job_list(self):
        try:
            self.wait.until(EC.presence_of_all_elements_located(self.TITLE_NODES))
            return len(self.driver.find_elements(*self.TITLE_NODES)) > 0
        except TimeoutException:
            return False
