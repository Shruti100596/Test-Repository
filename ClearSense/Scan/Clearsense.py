from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")
time.sleep(5)

driver.get("https://botman.cleartrust.club/")
#driver.maximize_window(
email=driver.find_element(By.XPATH, '//*[@id="txtEmail"]')
email.send_keys("shrutik2@botman.ninja")
time.sleep(5)

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

#Cleartrack dropdown icon
#cleartrack=driver.find_element(By.XPATH, "/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[1]/div[1]/button/span")
#cleartrack.click()
#time.sleep(2)
