from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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

#Advanced= driver.find_element(By. XPATH, '//*[@id="details-button"]')
#Advanced.click()

#Proceed= driver.find_element(By. XPATH, '//*[@id="proceed-link"]')  
#Proceed.click()
#time.sleep(3)

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

#Click on dashboard module
#driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[2]/ul/li[2]/a/span").click()
#time.sleep(2)

#Click on scan module
try:
    # Wait for the element to be clickable
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[2]/ul/li[2]/a/span'))
    )
    element.click()
except Exception as e:
    # Fallback to JavaScript click if standard click fails
    element = driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[2]/ul/li[2]/a/span")
    driver.execute_script("arguments[0].click();", element)
time.sleep(20)

# Click on create new scan
driver.find_element(By.XPATH, '//*[@id="btnCreateScan"]/button/span[2]').click()
time.sleep(3)

#Add scan name
Scan_Name=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[1]/input")
Scan_Name.send_keys("CT-Redirect")
time.sleep(3)

#Add description
Description=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[2]/textarea")
Description.send_keys("This scan is regarding redirect")
time.sleep(90)



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
Tag.send_keys("CT Redirect-Scan, #Sportsphere website")
time.sleep(10)

#Select CT tracking link Scan type 

try:
    # Wait for the element to be present and visible
    radio_button = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[5]/div[1]/div[3]/p-radiobutton/div"))
    )

    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView(true);", radio_button)

    # Click using ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(radio_button).click().perform()
    print("Radio button clicked successfully.")
except Exception as e:
    print("Error interacting with the radio button:", e)


#radio_button = driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[5]/div[1]/div[3]/p-radiobutton/div/div[2]/span") 
#radio_button.click()

#Select CT Custom Tracking url
Custom_domain_url=driver.find_element(By.XPATH, "//input[@placeholder='https://www.customTrackingURL.com']")
Custom_domain_url.send_keys("https://www.cleartrust.biz")
time.sleep(3)

#Select CT Redirect Destination url
destination_url=driver.find_element(By.XPATH,"//input[@placeholder='https://www.destinationURL.com']")
destination_url.send_keys("https://www.sportsphere.live")
time.sleep(3)

#Start date
Start_date=driver.find_element(By.XPATH, "//input[@placeholder='Offer start date']")
Start_date.clear()

Start_date.send_keys("31-12-2024")
time.sleep(3)

#End date
End_date=driver.find_element(By.XPATH, "//input[@placeholder='Offer end date']")
End_date.clear()

End_date.send_keys("31-12-2024")
time.sleep(3)


#Create&share CTA
driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[2]/p-button/button").click()
time.sleep(3)

#Copy the scan code
#driver.find_element(By.XPATH, "//i[@class='pi pi-clone']").click()
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
