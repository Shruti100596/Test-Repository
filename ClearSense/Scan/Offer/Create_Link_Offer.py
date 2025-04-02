from config import get_webdriver, initialize_sheets
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
import pyperclip
import datetime  # Import datetime to use for timestamps
from selenium.common.exceptions import NoSuchElementException
# Main function to run the create offer club scenario
def run_create_links_club():
    sheet = initialize_sheets()
    anksdriver = get_webdriver()
    #start_date = datetime.now()
    #end_date = start_date + timedelta(days=6)
    #end_date_str = end_date.strftime("%Y-%m-%d")
    try:
        # Fetch values from Google Sheet
        url = sheet.cell(2,11).value
        uname = sheet.cell(3, 11).value
        pwd = sheet.cell(4,11).value
        offer_name = sheet.cell(5, 11).value
        url_value = sheet.cell(6, 11).value
        #revenue = sheet.cell(7, 9).value
        #payout_for_affiliate = sheet.cell(8, 9).value
        # Navigate to URL
        anksdriver.get(url)
        anksdriver.maximize_window()
        # Login Scenario
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[1]/div/input').send_keys(uname)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[2]/div/input').send_keys(pwd)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[3]/p-checkbox/div/div[2]').click()
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[4]').click()
        time.sleep(5)
        # Create link
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[1]/div[1]/button/span').click()
        time.sleep(5)
        anksdriver.find_element(By.XPATH,'/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[1]/div[2]/ul/li[1]/button/span').click()
        time.sleep(5)
        anksdriver.find_element(By.XPATH,'/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[1]/div[2]/ul/div[1]/ul/li/a').click()
        time.sleep(2)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-layout/main/div/div[2]/app-create-fast-link/div/div/div[1]/form/p-accordion/div/p-accordiontab[1]/div/div[2]/div/div[1]/input').send_keys(offer_name)
        time.sleep(5)
        end_date = anksdriver.find_element(By.XPATH,'/html/body/app-root/app-layout/main/div/div[2]/app-create-fast-link/div/div/div[1]/form/p-accordion/div/p-accordiontab[1]/div/div[2]/div/div[2]/div[2]/p-calendar/span/input')
        end_date.click()
        time.sleep(3)
        end_next_date = anksdriver.find_element(By.XPATH,'/html/body/app-root/app-layout/main/div/div[2]/app-create-fast-link/div/div/div[1]/form/p-accordion/div/p-accordiontab[1]/div/div[2]/div/div[2]/div[2]/p-calendar/span/div/div/div/div[1]/button[2]')
        end_next_date.click()
        time.sleep(3)
        end_date_select=anksdriver.find_element(By.XPATH,'/html/body/app-root/app-layout/main/div/div[2]/app-create-fast-link/div/div/div[1]/form/p-accordion/div/p-accordiontab[1]/div/div[2]/div/div[2]/div[2]/p-calendar/span/div/div/div/div[2]/table/tbody/tr[4]/td[4]/span')
        end_date_select.click() #//*[@id="p-accordiontab-24-content"]/div/div[2]/div[2]/p-calendar/span/div/div/div/div[2]/table/tbody/tr[5]/td[6]/span
        time.sleep(3)
        anksdriver.find_element(By.XPATH, '//*[@id="p-accordiontab-0-content"]/div/div[3]/div/input').send_keys(url_value)
        time.sleep(3)
        quality_score_macros = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-1-content"]/div/div/p-inputswitch/div/span')
        quality_score_macros.click()
        time.sleep(3)
        enable_fraud_scanning = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div/div/p-inputswitch/div/span')
        enable_fraud_scanning.click()
        time.sleep(3)
        # Submit the offer
        anksdriver.find_element(By.XPATH, '//*[@id="submitButton"]/button/span').click()
        time.sleep(2)
        # Wait for offer creation to finish and capture the result
        time.sleep(5)  # Example wait time, adjust as necessary for your application
        result_message = "Offer is created successfully!"
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result_message = f"Offer is created successfully! at {now} "
        print(result_message)
        sheet.update_cell(2, 12, result_message)
         # Wait for offer creation to finish and capture the result
        time.sleep(5)  # Example wait time, adjust as necessary for your application
        result_message = "Offer is created successfully!"
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result_message = f"{offer_name} Offer is created successfully! at {now} "
        print(result_message)
        #sheet.update_cell(2, 10, result_message)
        copy_button = anksdriver.find_element(By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-fastlink-details/div/div[1]/div[2]/div[1]/div/p-button/button/span ')
        copy_button.click()
        time.sleep(5)
        copied_url = pyperclip.paste()                 #https://dev.fst.ink/Fx8w0Ow?ct_affid={ct_affid}&ct_sub_affid={ct_sub_affid}
        anksdriver.get(copied_url)
        sheet.update_cell(2,12 , result_message)
        return result_message
    finally:
        anksdriver.quit()
if __name__ == '__main__':
    run_create_links_club()
