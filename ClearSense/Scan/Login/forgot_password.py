def run_forgot_password():
  import time
  import sys
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.action_chains import ActionChains
  # Initialize WebDriver and ActionChains
  anksdriver = webdriver.Chrome()
  actions = ActionChains(anksdriver)

  # Visit the website
  anksdriver.get("https://sfolkar.cleartrust.club")
  anksdriver.maximize_window()
  time.sleep(5)
  forgot_password=anksdriver.find_element(By.XPATH,'/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[3]/a')
  forgot_password.click()
  time.sleep(2)

  enteremail=anksdriver.find_element(By.XPATH,'/html/body/app-root/app-forgot-password/div/div/div/div[1]/div/form/div[1]/div/input')
  enteremail.send_keys('gpx8nc3vh1@sfolkar.com')
  time.sleep(7)

  resetpwd=anksdriver.find_element(By.XPATH,'/html/body/app-root/app-forgot-password/div/div/div/div[1]/div/form/div[2]')
  resetpwd.click()
  time.sleep(8)
  anksdriver.maximize_window() 
  time.sleep(10)
  return "Python Forgot password executed successfully!"
  #close browser
  anksdriver.quit()
