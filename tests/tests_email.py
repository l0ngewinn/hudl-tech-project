from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# email and password are stored locally in a separate file (variables.py) ignored by git
from variables import email, password

def test_blank_email(navigate_to_login, render_clear_inputs):
  # tests for valid username and valid password using login button
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys("")

  # sleep for visibility
  time.sleep(1)

  # inputs password into text box
  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys(password)

  # sleep for visibility
  time.sleep(1)

  # clicks the login button
  login_btn = driver.find_element(By.ID, "logIn")
  login_btn.click()

  time.sleep(3)
  driver.quit()
  return

def test_invalid_email(navigate_to_login, render_clear_inputs):
  # tests for valid username and valid password using login button
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys("longewinn@gmail.com")

  # sleep for visibility
  time.sleep(1)

  # inputs password into text box
  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys(password)

  # sleep for visibility
  time.sleep(1)

  # clicks the login button
  login_btn = driver.find_element(By.ID, "logIn")
  login_btn.click()

  time.sleep(3)
  driver.quit()
  return

def test_valid_email(navigate_to_login, render_clear_inputs):
  # tests for valid username and valid password using login button
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render and clears text boxes
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys(email)

  # sleep for visibility
  time.sleep(1)

  # inputs password into text box
  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys(password)

  # sleep for visibility
  time.sleep(1)

  # clicks the login button
  login_btn = driver.find_element(By.ID, "logIn")
  login_btn.click()

  time.sleep(3)
  driver.quit()
  return

def run_tests_email(navigate_to_login, render_clear_inputs):
  test_valid_email(navigate_to_login, render_clear_inputs)
  test_invalid_email(navigate_to_login, render_clear_inputs)
  test_blank_email(navigate_to_login, render_clear_inputs)
  return