from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait

import time
# email and password are stored locally in a separate file (variables.py) ignored by git
from variables import email, password

def test_login_button_fail(navigate_to_login, render_clear_inputs):
  # tests if login button works with incorrect credentials
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render and clears text boxes
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys("longewinn@gmail.com")

  # inputs password into text box
  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys("Password1")

  # clicks the login button
  login_btn = driver.find_element(By.ID, "logIn")
  login_btn.click()

  # wait for page to render error message
  time.sleep(5)

  # checks to see if the error message states unrecognizable email and password
  expected = "We don't recognize that email and/or password"
  actual = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[2]/p").text
  try:
    assert expected == actual
  except:
    print(f"Expected '{expected}' but got '{actual}'")
    driver.quit()
    return

  print("test_login_button_fail() passed!")

  driver.quit()
  return

def test_login_button_success(navigate_to_login, render_clear_inputs):
  # tests if login button works with valid credentials
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render and clears text boxes
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys(email)

  # inputs password into text box
  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys(password)

  # clicks the login button
  login_btn = driver.find_element(By.ID, "logIn")
  login_btn.click()

  # wait for page to render before grabbing url
  WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/nav[1]"))
  )
  # test if the user succuessfully logged in, it will take the user to Hudl's home page
  expected_url = "https://www.hudl.com/home"
  actual_url = driver.current_url
  try:
    assert expected_url == actual_url
  except:
    print("Expected url: {} but got: {}".format(expected_url, actual_url))
    driver.quit()
    return

  print("test_login_with_button_success() passed!")

  driver.quit()
  return

def run_tests_login_button(navigate_to_login, render_clear_inputs):
  test_login_button_success(navigate_to_login, render_clear_inputs)
  test_login_button_fail(navigate_to_login, render_clear_inputs)
  return