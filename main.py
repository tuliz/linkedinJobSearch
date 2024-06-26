from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
EMAIL = ''
PASSWORD = ''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3929797925&f_AL=true&geoId=101620260&keywords=Python%20Developer&location=Israel&origin=JOB_SEARCH_PAGE_JOB_FILTER')

# Go to the sign in page
signin = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')
signin.click()

# Pass the Email and password to the user and password field and log in
username_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')
username_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD, Keys.ENTER)

# Get all the jobs showing up on page
jobs_list = driver.find_elements(By.CSS_SELECTOR, 'div[data-view-name="job-card"]')

# Start parsing the Jobs in a loop
for job in jobs_list:
    time.sleep(2)
    # Get the job id
    job_id = job.get_attribute('data-job-id')
    # Check if in the text of the job there is Easy apply, if not dismiss the job
    if not 'Easy Apply' in job.text:
        dismiss = driver.find_element(By.CSS_SELECTOR, f'div[data-job-id="{job_id}"] button')
        dismiss.click()
    else:
        job.click()
        time.sleep(5)
        #Find the Apply job button and click it
        job_apply_btn = driver.find_element(By.CSS_SELECTOR, f'button[data-job-id="{job_id}"]')
        job_apply_btn.click()
        # There are times you need to press twice Next buttons
        for n in range(2):
            # Check if there is next button if not break from loop
            try:
                next_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Continue to next step"]')
                next_btn.click()
            except:
                break
        # There are times there is a submit button on the first window, check if there is review button
        try:
            review_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Review your application"]')
            review_btn.click()
        except:
            pass
        # Get the submit button and click it
        submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Submit application"]')
        submit_btn.click()
        time.sleep(1)
        # Get the dismiss button and close the window of the apply job
        dismiss_btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss"]')
        dismiss_btn.click()
        time.sleep(1)
        # Get the dismiss button of the job applied to and click it
        dismiss = driver.find_element(By.CSS_SELECTOR, f'div[data-job-id="{job_id}"] button')
        dismiss.click()