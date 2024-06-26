from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3929797925&f_AL=true&geoId=101620260&keywords=Python%20Developer&location=Israel&origin=JOB_SEARCH_PAGE_JOB_FILTER')


