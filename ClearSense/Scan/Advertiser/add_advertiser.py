from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://cleartrust.cleartrust.club/app/offers")
#driver.maximize_window()
email=driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']")
email.send_keys("shalini@cleartrust.club")
time.sleep(3)

password=driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("shalini@123")

#eye icon
driver.find_element(By.XPATH, "//i[@class='pi pi-eye p-clickable absolute top-3/4 right-0 px-3']").click()
time.sleep(3)

#rememmber me 
driver.find_element(By.XPATH, "//div[@class='p-checkbox-box']").click()
time.sleep(3)

#Login CTA
driver.find_element(By.XPATH, "//div[@class='w-full mb-12 relative']").click()
time.sleep(5)

#Cleartrack dropdown icon
cleartrack=driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[1]/div[1]/button/span")
cleartrack.click()
time.sleep(2)

#Advertiser
Advertiser=driver.find_element(By.XPATH, "//span[normalize-space()='Advertisers']")
Advertiser.click()
time.sleep(2)

New_Advertiser=driver.find_element(By.XPATH, "//p-button[@class='p-element flex-grow sm:flex-grow-0']")
New_Advertiser.click()

Ad_Name=driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/div/div[2]/app-advertisers/p-dialog/div/div/div[3]/app-add-advertiser/form/div[2]/input")
Ad_Name.send_keys("Samsung")
time.sleep(2)

Ad_email=driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/div/div[2]/app-advertisers/p-dialog/div/div/div[3]/app-add-advertiser/form/div[3]/input")
Ad_email.send_keys("Supportsamsung@ctx.com")
time.sleep(2)

#CTA
driver.find_element(By.XPATH, "//p-button[@type='submit']").click()
time.sleep(2)

# Click the close button on the modal
wait = WebDriverWait(driver, 10)
close_button=wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "p-dialog-header-close-icon")))
close_button.click()
time.sleep(2)

# Search for the advertiser
#driver.find_element(By.XPATH, '//*[@id="pr_id_414"]/div[1]/div/span/input').click()
search_box=driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_box.send_keys("manish@botman.ninja")
time.sleep(4)

# Close the WebDriver
driver.close()

