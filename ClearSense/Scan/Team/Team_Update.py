from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Define the service pointing to the running ChromeDriver
service = Service('/Users/shrutikamble/bin/chromedriver')  
driver = webdriver.Chrome(service=service)

# Example: Open a website
driver.get("https://www.google.com")
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(2)

#open botman url
driver.get("https://botman.cleartrust.club/")
time.sleep(2)

#Add email
email=driver.find_element(By.XPATH, '//*[@id="txtEmail"]')
email.send_keys("shrutik2@botman.ninja")
time.sleep(2)

#Add password
password=driver.find_element(By.XPATH, '//*[@id="txtPassword"]')
password.send_keys("Test@123")
time.sleep(2)

#eye icon
driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div[1]/div/form/div[2]/div/i[2]").click()
time.sleep(2)

#rememmber me 
driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div[1]/div/form/div[3]/p-checkbox/div/div[2]").click()
time.sleep(2)

#Login CTA
driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div[1]/div/form/div[4]").click()
time.sleep(5)

#Click on scan module
try:
    # Wait for the element to be clickable
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[2]/ul/li[2]/a/span"))
    )
    element.click()
except Exception as e:
    # Fallback to JavaScript click if standard click fails
    element = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[2]/ul/li[2]/a/span")
    driver.execute_script("arguments[0].click();", element)
time.sleep(10)

#Click on Teams
Teams= driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[3]/div[1]/a/span")
Teams.click()
time.sleep(5)

#Click on Update
update_team= driver.find_element(By.XPATH, '//tbody/tr[1]/td[9]/p-button[1]/button[1]/span[2]')
update_team.click()
time.sleep(5)

##update team name
Team_name= driver.find_element(By.XPATH, '//*[@id="teamName"]')
Team_name.clear()
time.sleep(2)
Team_name.send_keys("Quality Assurance")
time.sleep(5)

#Update location
# Wait for the dropdown to be clickable and click it
try:
    Select_Location = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pr_id_27_label"]/div'))
    )
    Select_Location.click()
except TimeoutException:
    print("Dropdown for selecting location did not become clickable.")
    driver.save_screenshot("error_select_location.png")  # Capture screenshot for debugging
    raise
# Wait for the specific dropdown option to appear and click it
try:
    dropdown_Location = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Honduras')]"))
    )
    dropdown_Location.click()
except TimeoutException:
    print("Dropdown option did not appear or was not clickable.")
    driver.save_screenshot("error_dropdown_location.png")  # Capture screenshot for debugging
    raise
time.sleep(3)

#permission
permission= driver.find_element(By.XPATH, "//span[normalize-space()='Permissions']")
permission.click()
time.sleep(5)

#disable scan1 Permission
toggle1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="p-accordiontab-0-content"]/div/div/table/tbody/tr[2]/td/div/p-inputswitch/div/span'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not toggle1.is_selected():
    toggle1.click()  # Enable it
    print("Toggle enabled.")
else:
    toggle1.click()  # Disable it
    print("Toggle disabled.")    

#Update Scan2 Permission
toggle1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="p-accordiontab-0-content"]/div/div/table/tbody/tr[2]/td/div/p-inputswitch/div/span'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not toggle1.is_selected():
    toggle1.click()  # Enable it
    print("Toggle enabled.")
else:
    toggle1.click()  # Disable it
    print("Toggle disabled.")
time.sleep(5)

#Update
update= driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-team-add/div/div/p-button/button/span")
update.click()







