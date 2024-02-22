from selenium.webdriver.common.by import By

from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait

import time

from tests.tests_credentials import run_tests_credentials
from tests.tests_login_button import run_tests_login_button
from tests.tests_enter_key import run_tests_enter_key
from tests.tests_tab_key import run_tests_tab_key

def render_clear_inputs(driver):
  # wait for elements on login modal to render
  WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.ID, "email"))
  )
  WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.ID, "password"))
  )
  WebDriverWait(driver, 5).until(
  EC.presence_of_element_located((By.ID, "logIn"))
  )

  # makes sure text boxes are cleared for test
  driver.find_element(By.ID, "email").clear()
  driver.find_element(By.ID, "password").clear()
  return

def navigate_to_login(driver):
  # naviagates driver to login page
  driver.get("https://www.hudl.com/")
  # wait for login dropdown to render
  WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]"))
  )
  # sleep for visibility
  time.sleep(0.5)
  # selects the dropdown
  login_dropdown = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]")
  login_dropdown.click()
  # wait for element hudl login button to render
  WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div/div/div/a[1]"))
  )
  # sleep for visibility
  time.sleep(0.5)
  # selects the hudl login to navigate to login page
  hudl_login = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div/div/div/a[1]")
  hudl_login.click()
  return

def main():
  # run_tests_credentials(navigate_to_login, render_clear_inputs)
  # run_tests_login_button(navigate_to_login, render_clear_inputs)
  # run_tests_enter_key(navigate_to_login, render_clear_inputs)
  run_tests_tab_key(navigate_to_login, render_clear_inputs)

if __name__ == "__main__":
    main()