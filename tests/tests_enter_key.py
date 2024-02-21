from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# email and password are stored locally in a separate file (variables.py) ignored by git
from variables import email, password

def run_tests_enter_key(navigate_to_login, render_clear_inputs):
  return