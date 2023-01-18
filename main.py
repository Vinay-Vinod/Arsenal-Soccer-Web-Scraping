from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
from tabulate import tabulate

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
driver = webdriver.Chrome()

driver.get(website)


amb = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')

amb.click()


box = driver.find_element(By.CLASS_NAME, 'panel-body')

dropdown = Select(box.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Spain')

time.sleep(5)

matches = driver.find_elements(By.CSS_SELECTOR, 'tr')


matches = [match.text for match in matches]


driver.quit()


df = pd.DataFrame({'goals': matches})
print(tabulate(df))
df.to_csv('results.csv', index=False)