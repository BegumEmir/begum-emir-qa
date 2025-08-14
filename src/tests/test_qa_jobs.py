import time
from src.pages.qa_jobs_page import QAJobsPage

def test_qa_jobs_flow(driver):
    page = QAJobsPage(driver)

    page.open()
    page.click_see_all_qa()
    page.filter_location_istanbul()

    assert page.has_job_list(), "İş listesi görünmüyor."