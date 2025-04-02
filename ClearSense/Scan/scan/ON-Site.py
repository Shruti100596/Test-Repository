from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
driver.find_element(By.XPATH, "//i[@class='pi pi-eye p-clickable absolute top-3/4 right-0 px-3']").click()
time.sleep(5)

#rememmber me 
driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div[1]/div/form/div[3]/p-checkbox/div/div[2]").click()
time.sleep(5)

#Login CTA
driver.find_element(By.XPATH, "/html/body/app-root/app-login/div/div/div[1]/div/form/div[4]").click()
time.sleep(5)

#Click on scan module
driver.fine_element(By.XAPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[2]/ul/li[2]/a/span").click()
time.sleep(2)

# Click on create new scan
driver.element(By.XAPATH, '//*[@id="btnCreateScan"]/button/span[2]').click()
time.sleep(2)

#Add scan name
Scan_Name=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[1]/input")
Scan_Name.send_keys("On-Site Scan-20Dec")

#Add description
Description=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[2]/textarea")
Description.send_keys("This scan is regardiing onsite")

#selecting Advertiser
Advertiser=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[3]/div/p-dropdown/div/span")
select = Select(Advertiser)
select.select_by_index("1")

#Add Tag Value
Tag=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[4]/p-chips/div/ul/li/input")
Tag.send_keys("Onsite Scan, #Sportsphere website")

#Select Scan type
radio_button = driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[1]/div[5]/div/div[1]/p-radiobutton/div/div[2]") 
radio_button.click() 

#Create&share CTA
driver.fine_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-scan-information/form/div[2]/p-button/button").click()

#Copy the scan code
driver.fine_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-send-email/div[1]/button/i").click()

#Share code via email
email_id=driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-send-email/div[2]/p-chips/div/ul/li/input")
email_id.send_keys("shruti@cleartrust.cc")

#Send to devloper code
driver.fine_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/app-create-scan/div/app-send-email/div[4]/p-button[1]/button/span[2]").click()


# Close the browser
#driver.quit()
