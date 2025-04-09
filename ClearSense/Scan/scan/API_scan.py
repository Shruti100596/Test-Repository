from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import TimeoutException

options = Options()
service = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

# Example: Open a website
time.sleep(3)

#maximize the window
driver.maximize_window()

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
    element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Scans']"))
    )
    element.click()
except Exception as e:
    # Fallback to JavaScript click if standard click fails
    element = driver.find_element(By.XPATH, "//span[normalize-space()='Scans']")
    driver.execute_script("arguments[0].click();", element)
time.sleep(5)

# Click on create new scan
driver.find_element(By.XPATH, '//*[@id="btnCreateScan"]/button/span[2]').click()
time.sleep(3)

#Add scan name
Scan_Name=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[1]/input")
Scan_Name.send_keys("API Scan-1")
time.sleep(3)

#Add description
Description=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[2]/textarea")
Description.send_keys("This scan is regarding API Scan")
time.sleep(5)

#selecting Advertiser
# Wait for the dropdown to be clickable and click it
Select_Advertiser = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[3]/div/p-dropdown/div/span'))
)
Select_Advertiser.click()

# Wait for the specific dropdown option to appear and click it
dropdown_Category = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='ng-star-inserted'][normalize-space()='Krayons']"))
)
dropdown_Category.click()
time.sleep(3)

#Add Tag Value
Tag=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[4]/p-chips/div/ul/li/input")
Tag.send_keys("CT API-Scan")
time.sleep(5)


try:
    # Wait for the element to be present and visible
    radio_button = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[5]/div[1]/div[5]/p-radiobutton/div/div[2]"))
    )
   
    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", radio_button)

#Click using ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(radio_button).click().perform()
    print("Radio button clicked successfully.")
except Exception as e:
    print("Error interacting with the radio button:", e)
time.sleep(5) 

#select  API
API = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[5]/p-dropdown/div/div[2]"))
)
API.click()
time.sleep(5)

# Wait for the specific dropdown option to appear and click it
dropdown_API = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Helsinki']"))
)
dropdown_API.click()
time.sleep(3)

#Select Inventory
Select_Inventory=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[5]/div[2]/div/p-dropdown/div/div[2]"))
)
Select_Inventory.click()
time.sleep(3)

# Wait for the specific dropdown option to appear and click it
dropdown_inv = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Video']"))
)
dropdown_inv.click()
time.sleep(3)

# ✅ Step 1: Click the Trap Profile dropdown
try:
    trap_profile_dropdown = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[5]/div[3]/div/p-dropdown/div/div[2]"))
    )
    trap_profile_dropdown.click()
except TimeoutException:
    print("❌ Trap Profile dropdown icon was not found or not clickable.")
time.sleep(3)

# ✅ Step 2: Select the dropdown option: My trap options
try:
    dropdown_profile_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='My trap options']"))
    )
    dropdown_profile_option.click()
except TimeoutException:
    print("❌ 'My trap options' was not found or not clickable.")
time.sleep(3)

# ✅ Step 3: Click the trap profile selector (again if needed)
try:
    select_trap_profile = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[5]/div[4]/div/p-dropdown/div/div[2]"))
    )
    select_trap_profile.click()
except TimeoutException:
    print("❌ Trap profile dropdown (second click) was not found or not clickable.")
time.sleep(3)

# ✅ Step 4: Select the trap profile value: API-IN APP
try:
    dropdown_trap_profile_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Test trap-POP & video']"))
    )
    dropdown_trap_profile_option.click()
except TimeoutException:
    print("❌ 'API-IN APP' option was not found or not clickable.")
# Optional delay to let the selection settle
time.sleep(3)
 
#Create&share CTA
driver.find_element(By.XPATH, "//span[normalize-space()='Create & Share']").click()
time.sleep(3)

#Copy the scan code
try:
    button_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-send-email/div[1]/button/i"))
    )
    button_icon.click()
except Exception as e:
    print("Error locating or interacting with the element:", e)
time.sleep(3)

#Share code via email
email_id=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-send-email/div[2]/p-chips/div/ul/li/input")
email_id.send_keys("shruti@cleartrust.cc")
time.sleep(5)

driver.find_element(By.XPATH, "//label[normalize-space()='Message']").click()
time.sleep(5)

# submit CTA
Finish_CTA = driver.find_element(By.XPATH, "//span[normalize-space()='Skip & Finish']")
Finish_CTA.click()


# Close the browser
#driver.quit()
