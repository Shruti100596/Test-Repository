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
                       
#Open a website
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

#Click on Billing module
Billing_module=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Billing']"))
)    
Billing_module.click()
time.sleep(5)

#Download single pdf
Download=driver.find_element(By.XPATH, "//tbody/tr[1]/td[7]/div[1]/button[1]/span[2]")
Download.click()
time.sleep(5)

#Return back to webpage
original_tab = driver.current_window_handle

# Wait for the new tab to open and switch to it
WebDriverWait(driver, 10).until(lambda d: len(driver.window_handles) > 1)
new_tab = [handle for handle in driver.window_handles if handle != original_tab][0]
driver.switch_to.window(new_tab)

#PDF opened tab will get close
driver.close()

#switch to previous page
driver.switch_to.window(original_tab)

#Download Multiple pdfs
Select_all=driver.find_element(By.XPATH, "//div[@class='p-checkbox-box']")
Select_all.click()
time.sleep(5)

Download_all= driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/div/div[2]/app-billing/div/div[2]/div[1]/button/span[2]")
Download_all.click()
time.sleep(3)

# Close the browser
#driver.close()
