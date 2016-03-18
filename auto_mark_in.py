from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *


username_id = 'User_Name'
password_id = 'Password'
markin_link_txt = 'Mark In'
markin_id = 'markmein'

driver = webdriver.Firefox()
driver.get(home)
assert ":: EmployWise ::" in driver.title
username = driver.find_element_by_id(username_id)
password = driver.find_element_by_id(password_id)
username.send_keys(empid)
password.send_keys(emppassword, Keys.RETURN)
if 'Quick Mark In and Out' == str(driver.title):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, markin_id))
        )
        mark_in_div = driver.find_element_by_id(markin_id)
        mark_in_ele = mark_in_div.find_element_by_link_text(markin_link_txt)
        mark_in_ele.click()
        driver.close()
    finally:
        driver.quit()
