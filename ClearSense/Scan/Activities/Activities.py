from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the service pointing to the running ChromeDriver
service = Service('/Users/shrutikamble/bin/chromedriver')  
driver = webdriver.Chrome(service=service)
#driver.implicitly_wait(30)
                       
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

#Click on Activity module
Activity_module=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[4]/div[1]/a/span"))
)    
Activity_module.click()
time.sleep(5)

#Select All member
Select_all=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/main/div/div[2]/ct-activities/div/div/div[1]/div[2]/ct-activities-member-lists/div/p-checkbox/div/div[2]"))
)    
Select_all.click()
time.sleep(5)

#select Scan activity from dropdown
# Wait for the dropdown to be clickable and click it
Select_Activity = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='p-multiselect-trigger']"))
)
Select_Activity.click()

# Wait for the specific dropdown option to appear and click it
dropdown_Category = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Scan']//div[@class='p-checkbox-box']"))
)
dropdown_Category.click()
time.sleep(5)

#de-Select all member
Deselect_member=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/main/div/div[2]/ct-activities/div/div/div[1]/div[2]/ct-activities-member-lists/div/p-checkbox/div/div[2]"))
)    
Deselect_member.click()
time.sleep(3)

#Select one member
Select_member=driver.find_element(By.XPATH, "//li[3]//p-checkbox[1]//div[1]//div[2]")
Select_member.click()
time.sleep(3)

#clear scan the scan type
clear_scan = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//timesicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"))
)
clear_scan.click()
time.sleep(4)

#select report activity from dropdown
# Wait for the dropdown to be clickable and click it
Report= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='p-multiselect-trigger']"))
)
Report.click()
time.sleep(5)

# Wait for the specific dropdown option to appear and click it
Select_Report= WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Report']"))
)
Select_Report.click()
time.sleep(3)

#clear scan the scan type
clear_report = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//timesicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"))
)
clear_report.click()
time.sleep(3)

#select Team activity from dropdown
# Wait for the dropdown to be clickable and click it
Team= WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='p-multiselect-trigger']"))
)
Team.click()
time.sleep(5)
# Wait for the specific dropdown option to appear and click it
Select_Team= WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Team']//div[@class='p-checkbox-box']"))
)
Select_Team.click()
time.sleep(3)

#clear team the scan type
clear_Team = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//timesicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"))
)
clear_Team.click()
time.sleep(3)

#select Advertiser activity from dropdown
# Wait for the dropdown to be clickable and click it
Advertiser= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='p-multiselect-trigger']"))
)
Advertiser.click()
time.sleep(5)
# Wait for the specific dropdown option to appear and click it
Select_Advertiser= WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Advertisers']//div[@class='p-checkbox-box']"))
)
Select_Advertiser.click()
time.sleep(3)

#clear scan the scan type
clear_Advertiser = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//timesicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']"))
)
clear_Advertiser.click()
time.sleep(3)

#Deselect the team member
Deselect_member=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/main/div/div[2]/ct-activities/div/div/div[1]/div[2]/ct-activities-member-lists/div/p-checkbox/div/div[2]"))
)    
Deselect_member.click()
time.sleep(3)

#Search Options
Search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
Search.send_keys("scan")
time.sleep(5)

Search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
Search.clear()
time.sleep(3)
Search.send_keys("reports")
time.sleep(5)

Search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
Search.clear()
time.sleep(3)
Search.send_keys("team")
time.sleep(5)

Search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
Search.clear()
time.sleep(3)
Search.send_keys("advertiser")
time.sleep(5)

Search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
Search.clear()
time.sleep(3)
Search.send_keys("shruti")
time.sleep(5)

Search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
Search.clear()
time.sleep(3)
Search.send_keys("shalini")
time.sleep(5)

Search = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
Search.clear()
time.sleep(3)
Search.send_keys("retrieved")
time.sleep(5)
# Close the browser
driver.close()
