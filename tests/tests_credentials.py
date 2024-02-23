from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait

import time
# email and password are stored locally in a separate file (variables.py) ignored by git
from variables import email, password

def test_repeated_submission(navigate_to_login, render_clear_inputs):
  # tests for warning message for repeatedly submitting incorrect credentials
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys("lnguyen57@huskers.unl.edu")

  # sleep for visibility
  time.sleep(1)

  # inputs password into text box
  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys("password1")

  # sleep for visibility
  time.sleep(1)

  # clicks the login button
  login_btn = driver.find_element(By.ID, "logIn")
  for i in range(8):
    print(i)
    time.sleep(2)
    login_btn.click()
    ++i

  # wait for page to render error message
  time.sleep(5)

  # checks to see if the error message states unrecognizable email and password
  expected = "Too many logins with the same username or email."
  actual = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[2]/p").text
  try:
    assert expected == actual
  except:
    print(f"Expected '{expected}' but got '{actual}'")
    driver.quit()
    return

  print("test_repeated_submission() passed!")

  driver.quit()
  return

def test_password_change(navigate_to_login, render_clear_inputs):
  # tests if password change warning comes up
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys("johndoe@yahoo.com")

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

  # wait for page to render error message
  time.sleep(5)

  # checks to see if the error message states password change required
  expected = "Password change required."
  actual = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[2]/p").text
  try:
    assert expected == actual
  except:
    print(f"Expected '{expected}' but got '{actual}'")
    driver.quit()
    return

  print("test_password_change() passed!")

  driver.quit()
  return

def test_blank_password(navigate_to_login, render_clear_inputs):
  # tests if a blank password is caught, the field turns red, and the correct warning message appears
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys(email)

  # sleep for visibility
  time.sleep(1)

  # inputs password into text box
  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys("")

  # sleep for visibility
  time.sleep(1)

  # clicks the login button
  login_btn = driver.find_element(By.ID, "logIn")
  login_btn.click()

  time.sleep(2)

  # checks to see if blank text boxes bring up the required message
  required_message = "Required"
  required_message_password = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/form/div[3]/p").text
  try:
    assert required_message_password == required_message
  except:
    print("Password input does not warn that it is required")

  # chekcs to see if the correct error message comes up
  error_message_expected = "Please fill in all of the required fields"
  error_message_actual = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[2]/p").text
  try:
    assert  error_message_expected == error_message_actual
  except:
    print(f"Expected '{error_message_expected}' but got '{error_message_actual}'")

  # checks to see if the input box turns red
  expected_color_password = "rgb(185, 24, 4)"
  actual_color_password = str(password_input.value_of_css_property("color"))
  try:
    assert expected_color_password == actual_color_password
  except:
    print("Password input did not turn red")
    driver.quit()
    return

  print("test_blank_password() passed!")

  driver.quit()
  return

def test_invalid_password(navigate_to_login, render_clear_inputs):
  # tests for warning message for an invalid password
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys(email)

  # sleep for visibility
  time.sleep(1)

  # inputs password into text box
  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys("password1")

  # sleep for visibility
  time.sleep(1)

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

  print("test_invalid_password() passed!")

  driver.quit()
  return

def test_blank_email(navigate_to_login, render_clear_inputs):
  # tests if a blank email is caught, an error message pops up, and the field turns red
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

  time.sleep(2)

  # checks to see if blank text boxes bring up the required message
  required_message_expected = "Required"
  required_message_actual = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/form/div[1]/p[1]").text
  try:
    assert required_message_actual == required_message_expected
  except:
    print("Email input does not warn that it is required")

  # checks to see if the correct error message comes up
  error_message_expected = "Please fill in all of the required fields"
  error_message_actual = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[2]/p").text
  try:
    assert  error_message_expected == error_message_actual
  except:
    print(f"Expected '{error_message_expected}' but got '{error_message_actual}'")

  # checks to see if the input boxes turn red
  expected_color_email = "rgb(185, 24, 4)"
  actual_color_email = str(email_input.value_of_css_property("color"))
  try: 
    assert expected_color_email == actual_color_email
  except:
    print("Email input did not turn red")
    driver.quit()
    return

  print("test_blank_email() passed!")

  driver.quit()
  return

def test_invalid_email_format(navigate_to_login, render_clear_inputs):
  #tests if the field will accept an invalid email format
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys(">>><<<'''@hotmail.com")

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

  # wait for page to render error message
  time.sleep(5)

  # checks to see if the error message states unrecognizable email 
  expected = "We don't recognize that email and/or password"
  actual = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[2]/p").text
  try:
    assert expected == actual
  except:
    print(f"Expected '{expected}' but got '{actual}'")
    driver.quit()
    return

  print("test_invalid_email_format() passed!")

  driver.quit()
  return

def test_invalid_email_script(navigate_to_login, render_clear_inputs):
  # tests if the field will accept an invalid email and if it will run a script if given
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render
  render_clear_inputs(driver)

  # inputs email into text box
  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys("longe<script>alert('script')</script>winn@gmail.com")

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

  # wait for page to render error message
  time.sleep(5)

  # checks to see if the error message states unrecognizable email 
  expected = "We don't recognize that email and/or password"
  actual = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[2]/p").text
  try:
    assert expected == actual
  except:
    print(f"Expected '{expected}' but got '{actual}'")
    driver.quit()
    return

  print("test_invalid_email_script() passed!")

  driver.quit()
  return

def test_valid_credentials(navigate_to_login, render_clear_inputs):
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
    "Expected url: {} but got: {}".format(expected_url, actual_url)
    driver.quit()
    return

  print("test_valid_credentials() passed!")
  driver.quit()
  return

def run_tests_credentials(navigate_to_login, render_clear_inputs):
  test_valid_credentials(navigate_to_login, render_clear_inputs)
  test_invalid_email_script(navigate_to_login, render_clear_inputs)
  test_invalid_email_format(navigate_to_login, render_clear_inputs)
  test_blank_email(navigate_to_login, render_clear_inputs)
  test_invalid_password(navigate_to_login, render_clear_inputs)
  test_blank_password(navigate_to_login, render_clear_inputs)
  test_password_change(navigate_to_login, render_clear_inputs)
  test_repeated_submission(navigate_to_login, render_clear_inputs)
  return