from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
import time

username_id = 'User_Name'
password_id = 'Password'
markout_link_txt = 'Mark Out Now'
markout_id = 'markout_div'

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
            EC.presence_of_element_located((By.ID, markout_id))
        )
        mark_out_div = driver.find_element_by_id(markout_id)
        mark_out_ele = mark_out_div.find_element_by_link_text(markout_link_txt)
        mark_out_ele.click()
        time.sleep(60)
        driver.close()
    finally:
        driver.quit()

elif 'Welcome' == str(driver.title):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, 'inout'))
        )
        mark_out_div = driver.find_element_by_id('inout')
        mark_out_ele = mark_out_div.find_element_by_link_text('Now')
        mark_out_ele.click()
        time.sleep(60)
        driver.close()
    finally:
        driver.quit()
