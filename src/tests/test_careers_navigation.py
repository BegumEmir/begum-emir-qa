import time
from src.pages.home_page import HomePage
from src.pages.careers_page import CareersPage

def test_careers_navigation(driver):
    home = HomePage(driver)
    careers = CareersPage(driver)

    home.open()
    assert home.is_loaded(), "Homepage not loaded"

    home.navigate_to_careers()
    time.sleep(2)

    assert careers.is_loaded(), "Careers page not loaded"
    assert careers.are_blocks_visible(), "Some content blocks are missing"
