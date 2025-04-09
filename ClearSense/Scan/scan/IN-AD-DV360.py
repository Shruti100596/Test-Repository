from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

# Define the service pointing to the running ChromeDriver
service = Service('/Users/shrutikamble/bin/chromedriver')  
driver = webdriver.Chrome(service=service)

# Example: Open a website
driver.get("https://www.google.com")
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
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[2]/ul/li[2]/a/span"))
    )
    element.click()
except Exception as e:
    # Fallback to JavaScript click if standard click fails
    element = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[2]/ul/li[2]/a/span")
    driver.execute_script("arguments[0].click();", element)
time.sleep(5)


#driver.set_page_load_timeout(60)  # Set timeout to 120 seconds

# Click on create new scan
driver.find_element(By.XPATH, "//span[@class='p-button-label ng-star-inserted']").click()
time.sleep(3)

#Add scan name
Scan_Name=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[1]/input")
Scan_Name.send_keys("IN-AD-6Jan")
time.sleep(3)

#Add description
Description=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[2]/textarea")
Description.send_keys("This scan is regarding IN-AD")
time.sleep(10)

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
Tag.send_keys("Onsite Scan, #Sportsphere website")
time.sleep(2)

#Select Scan type
radio_button = driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[5]/div[1]/div[2]/p-radiobutton/div/div[2]/span") 
radio_button.click()
time.sleep(10)

driver.find_element(By.Xpath, "//div[@class='p-radiobutton-box p-highlight p-focus']//span[@class='p-radiobutton-icon']").click()

#Create&share CTA
driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[2]/p-button/button").click()
time.sleep(3)

#Copy the scan code
try:
    button_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-send-email/div[1]/button/i"))
    )
    button_icon.click()
except Exception as e:
    print("Error locating or interacting with the element:", e)

#Share code via email
email_id=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-send-email/div[2]/p-chips/div/ul/li/input")
email_id.send_keys("shruti@cleartrust.cc")
time.sleep(7)

driver.find_element(By.XPATH, "//label[normalize-space()='Message']").click()

# submit CTA
Finish_CTA = driver.find_element(By.XPATH, "//span[normalize-space()='Skip & Finish']")
Finish_CTA.click()


# Close the browser
#driver.quit()
