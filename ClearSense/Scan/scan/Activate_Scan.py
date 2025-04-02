from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver import ActionChains
#from selenium.common.exceptions import TimeoutException
import time



options = Options()
service = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

# Example: Open a website
#driver.get("https://www.google.com")
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
time.sleep(10)

#Deactivate scan name
Deactivate_scan=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/app-root[1]/app-layout[1]/main[1]/div[1]/div[2]/app-scans[1]/div[1]/div[1]/p-table[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[11]/p-button[1]/button[1]"))
   )                            
Deactivate_scan.click()
time.sleep(5)

#Yes Option
Yes=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/main/div/div[2]/app-scans/p-confirmdialog/div/div/div[3]/button[2]"))
   )                            
Yes.click()
time.sleep(5)

#Activate scan name
Activate_scan=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/app-root[1]/app-layout[1]/main[1]/div[1]/div[2]/app-scans[1]/div[1]/div[1]/p-table[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[11]/p-button[1]/button[1]'))
   )                    
Activate_scan.click()
time.sleep(3)

#Yes Option
Yes=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/main/div/div[2]/app-scans/p-confirmdialog/div/div/div[3]/button[2]"))
   )                            
Yes.click()
time.sleep(5)

#Get Code
Code = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//tbody/tr[1]/td[11]/p-button[2]/button[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", Code)

# Try standard click
try:
        Code.click()
        print("Button clicked successfully.")
except:
        # Fallback to JavaScript click
        driver.execute_script("arguments[0].click();", Code)
        print("Button clicked successfully using JavaScript.")

time.sleep(5)

#Copy the scan code
#driver.find_element(By.XPATH, "//i[@class='pi pi-clone']").click()
try:
    button_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-send-email/div[1]/button"))
    )
    button_icon.click()
except Exception as e:
    print("Error locating or interacting with the element:", e)

#Share code via email
try:
    # Wait for the element to be present and visible
    email_id = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-send-email/div[2]/p-chips/div/ul/li/input"))
    )
    print("Element is visible.")
    email_id.send_keys("shruti@cleartrust.cc")

except Exception as e:
    print("Error locating the element:", e)
    print("Page Source:", driver.page_source)
time.sleep(7)

driver.find_element(By.XPATH, "//label[normalize-space()='Message']").click()

# submit CTA
Finish_CTA = driver.find_element(By.XPATH, "//span[normalize-space()='Skip & Finish']")
Finish_CTA.click()


# Close the browser
#driver.quit()
