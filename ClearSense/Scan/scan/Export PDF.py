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


#select Scan from dropdown
Scan_dropdown=WebDriverWait(driver, 20).until(
       EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-layout/main/div/div[2]/app-executive-dashboard/div/div[1]/div[1]/div/p-dropdown[1]/div/span"))
)
Scan_dropdown.click()
time.sleep(3)

option = WebDriverWait(driver, 20).until(
  EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Quarter 2024']"))
  )
option.click()
time.sleep(60)

#CLICK ON APPLY
apply= driver.find_element(By. XPATH, "/html/body/app-root/app-layout/main/div/div[2]/app-executive-dashboard/div/div[1]/div[1]/p-button/button/span[2]")
apply.click()
time.sleep(5)

#scroll down
##driver.find_element(By.XPATH, '//*[@id="pr_id_19_label"]').click()
#driver.execute_script("window.scrollTo(0, 1000);")

#Export PDF
export= driver.find_element(By. XPATH, "/html/body/app-root/app-layout/main/div/div[2]/app-executive-dashboard/div/div[1]/div[2]/p-button/button/span[2]")
export.click()
