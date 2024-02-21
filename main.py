from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time
# email and password are stored locally in a separate file (variables.py) ignored by git
from variables import email, password

def test_invalid_user_invalid_pass_login_button():
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
  password_input.send_keys("password1")

  # sleep for visibility
  time.sleep(1)

  # clicks the login button
  login_btn = driver.find_element(By.ID, "logIn")
  login_btn.click()

  time.sleep(3)
  driver.quit()

def test_valid_user_valid_pass_login_button():
  # tests for valid username and valid password using login button
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
  password_input.send_keys(password)

  # sleep for visibility
  time.sleep(1)

  # clicks the login button
  login_btn = driver.find_element(By.ID, "logIn")
  login_btn.click()

  time.sleep(3)
  driver.quit()

def render_clear_inputs(driver):
  # wait for elements on login to render
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

def navigate_to_login(driver):
  # naviagets driver to login page
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

def main():
  test_valid_user_valid_pass_login_button()
  test_invalid_user_invalid_pass_login_button()

if __name__ == "__main__":
    main()