from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

options = Options()
service = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

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
time.sleep(10)


#Click on Teams
Teams= driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[1]/a/span")
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

# Export PDF
try:
    Export_PDF = driver.find_element(By.XPATH, "//span[normalize-space()='PDF']")
    Export_PDF.click()
    print("Clicked on Export PDF")
except Exception as e:
    print("Failed to click on PDF button:", e)

time.sleep(2)  # Just enough delay to let the browser respond

# Get the current window handle (original tab)
original_tab = driver.current_window_handle
print("Original tab:", original_tab)

try:
    # Wait for a new tab to open
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    print("New tab opened")
    
    new_tab = [handle for handle in driver.window_handles if handle != original_tab][0]
    driver.switch_to.window(new_tab)
    print("Switched to new tab")

    # Close the new tab
    driver.close()
    print("Closed the PDF tab")

    # Switch back to original tab
    driver.switch_to.window(original_tab)
    print("Switched back to original tab")

except TimeoutException:
    print("❌ Timeout: New tab did not open. PDF may have opened in same tab or was downloaded.")

except Exception as e:
    print("❌ Unexpected error:", e)

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
