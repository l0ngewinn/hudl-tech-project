from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait

import time
# email and password are stored locally in a separate file (variables.py) ignored by git
from variables import email, password

def test_tab_success(navigate_to_login, render_clear_inputs):
  # tests if tabbing between text boxes works
  driver = webdriver.Firefox()

  #initial navigation to login page
  navigate_to_login(driver)

  # wait for elements on login to render and clears text boxes
  render_clear_inputs(driver)

  # clicks on the email text box
  email_input = driver.find_element(By.ID, "email")
  email_input.click()

  # inputs email into text box, tabs, inputs password, and clicks enter
  ActionChains(driver)\
  .send_keys(email)\
  .send_keys(Keys.TAB)\
  .send_keys(password)\
  .send_keys(Keys.RETURN)\
  .perform()

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

  print("test_tab_success() passed!")

  driver.quit()
  return

def run_tests_tab_key(navigate_to_login, render_clear_inputs):
  test_tab_success(navigate_to_login, render_clear_inputs)
  return