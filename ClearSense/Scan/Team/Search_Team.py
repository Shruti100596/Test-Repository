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

#Search by Team name
team_name= driver.find_element(By.XPATH, "//input[@id='txtSearch']")
team_name.send_keys("Quality Assurance")
time.sleep(3)

#Clear the search
team_name.clear()

#Serch by Location
team_name.send_keys("India")
time.sleep(3)

#Clear the search
team_name.clear()

#Serch by Advertiser
team_name.send_keys("sj-advertiser74")
time.sleep(3)

#Clear the search
team_name.clear()

#Serch by Admin Name
team_name.send_keys("Shruti")
time.sleep(3)

#Clear the search
team_name.clear()

#Serch by Email
team_name.send_keys("shruti@cleartrust.cc")
time.sleep(3)

#Clear the search
team_name.clear()

#Serch by Number
team_name.send_keys("90")
time.sleep(3)

#Clear the search
team_name.clear()

#Serch by Tag
team_name.send_keys("gh")
time.sleep(3)

driver.quit()
