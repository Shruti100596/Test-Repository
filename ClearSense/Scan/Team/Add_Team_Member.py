from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Define the service pointing to the running ChromeDriver
service = Service('/usr/local/bin/chromedriver')  
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
email.send_keys("shruti@cleartrust.cc")
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
time.sleep(10)

#Click on Add new Team Member
Add_Team_Member= driver.find_element(By.XPATH, "//span[@class='p-button-label ng-star-inserted']")
Add_Team_Member.click()
time.sleep(3)

#Add Name
Name= driver.find_element(By.XPATH, "//input[@placeholder='John Doe']")
Name.send_keys("Anupama")
time.sleep(3)

#Add Email
Email= driver.find_element(By.XPATH, "//input[@placeholder='john.doe@example.com']")
Email.send_keys("Anupama@clertrust.cc")
time.sleep(3)

#Add Contact
Contact= driver.find_element(By.XPATH, "//input[@placeholder='+00-0000000000']")
Contact.send_keys("+908765739234")
time.sleep(3)

#Role
Role=driver.find_element(By.XPATH, "//div[@class='p-radiobutton-box']")
Role.click()
time.sleep(3)

#Add_Permission
Add_Permission= driver.find_element(By.XPATH, "//span[normalize-space()='Assign Permissions']")
Add_Permission.click()
time.sleep(3)

#disable offer Permission
toggle1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="p-accordiontab-0-content"]/div/div/table/tbody/tr[2]/td/div/p-inputswitch/div/span'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not toggle1.is_selected():
    toggle1.click()  # Enable it
    print("Toggle enabled.")
else:
    toggle1.click()  # Disable it
    print("Toggle disabled.")    
time.sleep(3)

#disable scan Permission
scan1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="p-accordiontab-1-content"]/div/div/table/tbody/tr[4]/td/div/p-inputswitch/div/span'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not scan1.is_selected():
    scan1.click()  # Enable it
    print("Toggle enabled.")
else:
    scan1.click()  # Disable it
    print("Toggle disabled.")  
time.sleep(3)

#disable scan Permission
scan2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/ct-team-member-add[1]/div[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/ct-team-member-permissions[1]/form[1]/p-accordion[2]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/p-inputswitch[1]/div[1]/span[1]"))#disable scan Permission
)                                              
# Check the current state and toggle
if not scan2.is_selected():
    scan2.click()  # Enable it
    print("Toggle enabled.")
else:
    scan2.click()  # Disable it
    print("Toggle disabled.")
time.sleep(4)

#Add Member
Add_Member= driver.find_element(By.XPATH, "/html/body/p-dynamicdialog/div/div/div[2]/ct-team-member-add/div/div/p-button/button/span")
Add_Member.click()
time.sleep(4)

#quit browser
driver.quit()

