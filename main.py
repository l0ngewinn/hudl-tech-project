from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time

def test_valid_user_valid_pass_login_button(driver):
   # tests for valid username and valid password using login button
   WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "email"))
  )
   email_input = driver.find_element(By.ID, "email")
   email_input.send_keys("")

   WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "password"))
  )
   password_input = driver.find_element(By.ID, "password")
   password_input.send_keys("")

   WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "logIn"))
  )
   login_btn = driver.find_element(By.ID, "logIn")
   login_btn.click()

def initialize_driver():
  # sets the firefox webdriver
  driver = webdriver.Firefox()
  # navigate to hudl.com
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
  return driver

def main():
  # sets driver from function
  driver = initialize_driver()

  test_valid_user_valid_pass_login_button(driver)

  time.sleep(5)
  driver.quit()
    

if __name__ == "__main__":
    main()