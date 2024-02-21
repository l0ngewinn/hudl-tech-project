from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time
from variables import email, password

def test_valid_user_valid_pass_login_button():
  driver = webdriver.Firefox()
  navigate_to_login(driver)

  # tests for valid username and valid password using login button
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

  email_input = driver.find_element(By.ID, "email")
  email_input.send_keys(email)

  password_input = driver.find_element(By.ID, "password")
  password_input.send_keys(password)

  login_btn = driver.find_element(By.ID, "logIn")
  login_btn.click()
  time.sleep(5)
  driver.quit()

def navigate_to_login(driver):
    # naviagets driver to login page
    driver.get("https://www.hudl.com/")
  # wait for the element to render
    WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]"))
    )
    # selects the dropdown
    login_dropdown = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]")
    login_dropdown.click()
    # wait for element to render
    WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div/div/div/a[1]"))
    )
    # selects the hudl login to navigate to login page
    hudl_login = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div/div/div/div/a[1]")
    hudl_login.click()

def main():
  test_valid_user_valid_pass_login_button()
    

if __name__ == "__main__":
    main()