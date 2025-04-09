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
time.sleep(10)

#Click on create new team
create_new_team= driver.find_element(By.XPATH, '//*[@id="btnCreateTeam"]/button/span[2]')
create_new_team.click()
time.sleep(3)

#Enter a team name
Team_name= driver.find_element(By.XPATH, '//*[@id="teamName"]')
Team_name.send_keys("Quality Control")
time.sleep(3)

#Enter a team description
Team_description= driver.find_element(By.XPATH, '//*[@id="description"]')
Team_description.send_keys("This team is associates with Quality Control")
time.sleep(3)

#Location
# Wait for the dropdown to be clickable and click it
try:
    Select_Location = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pr_id_27_label"]/div'))
    )
    Select_Location.click()
except TimeoutException:
    print("Dropdown for selecting location did not become clickable.")
    driver.save_screenshot("error_select_location.png")  # Capture screenshot for debugging
    raise

# Wait for the specific dropdown option to appear and click it
try:
    dropdown_Location = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Hong Kong']"))
    )
    dropdown_Location.click()
except TimeoutException:
    print("Dropdown option did not appear or was not clickable.")
    driver.save_screenshot("error_dropdown_location.png")  # Capture screenshot for debugging
    raise

# Add a small pause to stabilize actions (optional)
time.sleep(3)   

#Team_Size
# Wait for the dropdown to be clickable and click it
Select_TeamSize = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="pr_id_28_label"]/div'))
)
Select_TeamSize.click()

# Wait for the specific dropdown option to appear and click it
dropdown_TeamSize = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='Large']"))
)
dropdown_TeamSize.click()
time.sleep(3)

#Add a tag
Tag= driver.find_element(By.XPATH, "//input[@placeholder='Add tags']")
Tag.send_keys("Quality Control")
time.sleep(3)

#selecting Advertiser
# Wait for the dropdown to be clickable and click it
Select_Advertiser = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="pr_id_29_label"]/div'))
)
Select_Advertiser.click()

# Wait for the specific dropdown option to appear and click it
dropdown_Category = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@aria-label='sj-advertiser74']"))
)
dropdown_Category.click()
time.sleep(3)

#Enter Admin Name
Admin_Name= driver.find_element(By.XPATH, '//*[@id="adminName"]')
Admin_Name.send_keys("Shruti")
time.sleep(3)

#Enter Admin Email
Admin_email= driver.find_element(By.XPATH, '//*[@id="adminEmail"]')
Admin_email.send_keys("shruti1@offergrid.com")
time.sleep(3)

#Enter Admin Mobile No.
Admin_Mobile= driver.find_element(By.XPATH, "//input[@id='adminMobile']")
Admin_Mobile.send_keys("+913728974893")
time.sleep(3)

#Assign Permission
Assign_Permission=driver.find_element(By.XPATH, '//*[@id="btnAssignPermissions"]/button')
Assign_Permission.click()
time.sleep(3)

#Enable Permission
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

#Enable 2nd toggle
toggle2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="p-accordiontab-0-content"]/div/div/table/tbody/tr[3]/td/div/p-inputswitch/div/span'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not toggle2.is_selected():
    toggle2.click()  # Enable it
    print("Toggle enabled.")
else:
    toggle2.click()  # Disable it
    print("Toggle disabled.")  

#Enable 3rd toggle
toggle3 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="p-accordiontab-0-content"]/div/div/table/tbody/tr[4]/td/div/p-inputswitch/div/span'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not toggle3.is_selected():
    toggle3.click()  # Enable it
    print("Toggle enabled.")
else:
    toggle3.click()  # Disable it
    print("Toggle disabled.")

#Enable 4th toggle
toggle4 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/app-team-add[1]/div[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/ct-teams-permissions[1]/form[1]/p-accordion[1]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/p-inputswitch[1]/div[1]/span[1]'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not toggle4.is_selected():
    toggle4.click()  # Enable it
    print("Toggle enabled.")
else:
    toggle4.click()  # Disable it
    print("Toggle disabled.")

#Enable affiliate1 toggle
aff_toggle1 = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/app-team-add[1]/div[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/ct-teams-permissions[1]/form[1]/p-accordion[1]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[7]/td[1]/div[1]/p-inputswitch[1]/div[1]/span[1]'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not aff_toggle1.is_selected():
    aff_toggle1.click()  # Enable it
    print("Toggle enabled.")
else:
    aff_toggle1.click()  # Disable it
    print("Toggle disabled.")

#Enable affiliate2 toggle
aff_toggle2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//tbody/tr[8]/td[1]/div[1]/p-inputswitch[1]/div[1]/span[1]'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not aff_toggle2.is_selected():
    aff_toggle2.click()  # Enable it
    print("Toggle enabled.")
else:
    aff_toggle2.click()  # Disable it
    print("Toggle disabled.")
time.sleep(3) 

#Enable Scan1 toggle
Scan1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/app-team-add[1]/div[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/ct-teams-permissions[1]/form[1]/p-accordion[2]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/p-inputswitch[1]/div[1]/span[1]'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not Scan1.is_selected():
    Scan1.click()  # Enable it
    print("Toggle enabled.")
else:
    Scan1.click()  # Disable it
    print("Toggle disabled.") 

#Enable Scan4 toggle
Scan4 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/app-team-add[1]/div[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/ct-teams-permissions[1]/form[1]/p-accordion[2]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[7]/td[1]/div[1]/p-inputswitch[1]/div[1]/span[1]'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not Scan4.is_selected():
    Scan4.click()  # Enable it
    print("Toggle enabled.")
else:
    Scan4.click()  # Disable it

#Enable Advertiser1 toggle
Ad_toggle1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/app-team-add[1]/div[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/ct-teams-permissions[1]/form[1]/p-accordion[3]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/p-inputswitch[1]/div[1]/span[1]'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not Ad_toggle1.is_selected():
    Ad_toggle1.click()  # Enable it
    print("Toggle enabled.")
else:
    Ad_toggle1.click()  # Disable it
 

#Enable Advertiser2 toggle
Ad_toggle2 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[2]/app-team-add[1]/div[1]/p-tabview[1]/div[1]/div[2]/p-tabpanel[2]/div[1]/ct-teams-permissions[1]/form[1]/p-accordion[3]/div[1]/p-accordiontab[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/p-inputswitch[1]/div[1]/span[1]'))  # Replace with correct locator
)                                              
# Check the current state and toggle
if not Ad_toggle2.is_selected():
    Ad_toggle2.click()  # Enable it
    print("Toggle enabled.")
else:
    Ad_toggle2.click()  # Disable it
    print("Toggle disabled.")
time.sleep(3) 

#Click on Add Team
Add_Team= driver.find_element(By.XPATH, '//*[@id="btnAddTeam"]/button/span')
Add_Team.click()
time.sleep(5)

#Logout
Profile= driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/div/div[1]/app-header/nav/app-loggedin-profile/div/button")
Profile.click()
time.sleep(3)

Logout=driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/ul/li[3]/a")
Logout.click()
time.sleep(3)

#Quit browser
driver.quit()
