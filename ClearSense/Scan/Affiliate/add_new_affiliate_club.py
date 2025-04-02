import time
import datetime
from config import initialize_sheets, get_webdriver, By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
    
def run_add_new_affiliate():
    anksdriver = None 
    #anksdriver = webdriver.Chrome()
    #actions = ActionChains(anksdriver)
    
    
    # Initialize Google Sheets
    sheet = initialize_sheets()
        
    # Attempt to get the WebDriver

    anksdriver = get_webdriver()

    # Fetch credentials and URL
    anksdriver.implicitly_wait(5) 
    url = sheet.cell(2, 7).value
    print("the url is",url)
    username = sheet.cell(3, 7).value
    password = sheet.cell(4, 7).value
    affiliate_name = sheet.cell(5,7).value
    affiliate_email = sheet.cell(6,7).value

    # Start WebDriver and open URL
    anksdriver.get(url)
    print("Navigated to:", url)
    #time.sleep(10)
    #login and passwords keys
    anksdriver.maximize_window()

    uname = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[1]/div/input')
    uname.send_keys(username)
    time.sleep(3)
    pwd = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[2]/div/input')
    pwd.send_keys(password)
    time.sleep(3)

    tick_box=anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[3]/p-checkbox/div/div[2]')
    tick_box.click()
    time.sleep(3)

    enter = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[4]')
    enter.click()
    time.sleep(15)

    create_affiliate = anksdriver.find_element(By.XPATH,'/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[3]/div[1]/a/span')
    create_affiliate.click()
    time.sleep(5)

    new_affiliate = anksdriver.find_element(By.XPATH,'//*[@id="pr_id_16"]/div[1]/div/div/p-button/button/span[2]')
    new_affiliate.click()
    time.sleep(3)
    

    affi_name = anksdriver.find_element(By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-add-affiliate/form/div[2]/input')
    affi_name.send_keys( affiliate_name)
    time.sleep(2)

    affi_email = anksdriver.find_element(By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-add-affiliate/form/div[3]/input')
    affi_email.send_keys(affiliate_email)
    time.sleep(2)

    add_affiliate = anksdriver.find_element(By.XPATH, '/html/body/p-dynamicdialog/div/div/div[2]/app-add-affiliate/form/div[5]/p-button')
    add_affiliate.click()
    time.sleep(20)

    
    #close_cross = anksdriver.find_element(By.XPATH, '/html/body/p-dynamicdialog/div/div/div[1]/div/button/timesicon/svg')
    #close_cross.click()
    #time.sleep(3)

    close_button = anksdriver.find_element(By.CLASS_NAME, "p-dialog-header-close-icon")
    close_button.click()
    time.sleep(3)
    

    create_affiliate_add = anksdriver.find_element(By.XPATH,'/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[1]/a/span')
    create_affiliate_add.click()                                    
    
    anksdriver.maximize_window() 
    time.sleep(3)
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sheet.update_cell(2, 8, f"Login Successfully{now}")
    
    return "Python script executed successfully!" 

    anksdriver.quit()

















