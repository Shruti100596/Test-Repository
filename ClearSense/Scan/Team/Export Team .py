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

#Export file
Export=driver.find_element(By.XPATH, "//button[@type='button']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']")
Export.click()
time.sleep(5)

#Export CSV
Export_CSV=driver.find_element(By.XPATH, "//span[normalize-space()='CSV']")
Export_CSV.click()
time.sleep(5)


#Export file
Export=driver.find_element(By.XPATH, "//button[@type='button']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']")
Export.click()
time.sleep(5)

#Export PDF
Export_PDF=driver.find_element(By.XPATH, "//span[normalize-space()='PDF']")
Export_PDF.click()
time.sleep(5)

# Get the current window handle (original tab)
original_tab = driver.current_window_handle

# Wait for the new tab to open and switch to it
WebDriverWait(driver, 10).until(lambda d: len(driver.window_handles) > 1)
new_tab = [handle for handle in driver.window_handles if handle != original_tab][0]
driver.switch_to.window(new_tab)

#PDF opened tab will get close
driver.close()

#switch to previous page
driver.switch_to.window(original_tab)

#Export file
Export=driver.find_element(By.XPATH, "//button[@type='button']//chevrondownicon[@class='p-element p-icon-wrapper ng-star-inserted']//*[name()='svg']")
Export.click()
time.sleep(5)

#Export XLS
Export_XLS=driver.find_element(By.XPATH, "//span[normalize-space()='XLS']")
Export_XLS.click()
time.sleep(5)

#Quit Browser
driver.quit()
