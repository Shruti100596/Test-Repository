import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# Extract command line arguments
if len(sys.argv) != 4:
    print("Usage: script.py <business_name> <email_id> <password>")
    sys.exit(1)
business_name = sys.argv[1]
email_id = sys.argv[2]
password_1 = sys.argv[3]
print(business_name)
print(email_id)
print(password_1)

# Initialize WebDriver and ActionChains
driver = webdriver.Chrome()
actions = ActionChains(driver)

# Visit the websitedriver.get("https://www.cleartrust.app")
driver.maximize_window()
time.sleep(5)

# Create an account
create_an_account = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[5]/p/a')
create_an_account.click()
time.sleep(2)

# Input business name
business_name_field = driver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[1]/input')
business_name_field.send_keys(business_name)
time.sleep(2)

# Input email ID
email_id_field = driver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[2]/input')
email_id_field.send_keys(email_id)
time.sleep(2)

# Select agency
agency = driver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[3]/div/p-radiobutton[1]/div/div[2]/span')
agency.click()
time.sleep(2)
# Input password
password_field = driver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[4]/div/input')
password_field.send_keys(password_1)
time.sleep(2)
# Toggle password visibility
password_eye = driver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[4]/div/i')
password_eye.click()
time.sleep(2)
# Confirm password
confirm_password_field = driver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[5]/div/input')
confirm_password_field.send_keys(password_1)
time.sleep(2)
# Toggle confirm password visibility
confirm_password_eye = driver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[5]/div/i')
confirm_password_eye.click()
time.sleep(2)
# Agree to terms
agree_terms = driver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[6]/p-checkbox/div/div[2]')
agree_terms.click()
time.sleep(3)
# Sign up
sign_up_button = driver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[7]')
sign_up_button.click()
time.sleep(7)
print("sighing up")
# Log in
#driver.get("https://newclick.cleartrust.club")
#driver.maximize_window()
#time.sleep(5)
# Extract the domain name from email_id and create the dynamic URL
domain_name = email_id.split('@')[1].split('.')[0]
print(domain_name)
dynamic_url = f"https://{domain_name}.cleartrust.app"
# Log in with the dynamically created URL
driver.get(dynamic_url)
driver.maximize_window()
time.sleep(5)
# Input login name (email ID)
login_name_field = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[1]/div/input')
login_name_field.send_keys(email_id)
time.sleep(2)
# Input password for login
login_password_field = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[2]/div/input')
login_password_field.send_keys(password_1)
time.sleep(2)
# Remember me
remember_me_checkbox = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[3]/p-checkbox/div/div[2]')
remember_me_checkbox.click()
time.sleep(2)
# Click login button
login_button = driver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[4]')
login_button.click()
time.sleep(5)
# Close browser
driver.quit()
