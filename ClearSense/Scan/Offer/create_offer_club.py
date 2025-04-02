from config import get_webdriver, initialize_sheets
from selenium.webdriver.common.by import By
import time
import datetime  # Import datetime to use for timestamps
from selenium.common.exceptions import NoSuchElementException

# Main function to run the create offer club scenario
def run_createoffer_club():
    sheet = initialize_sheets()
    anksdriver = get_webdriver()
    try:
        # Fetch values from Google Sheet
        url = sheet.cell(2, 9).value
        uname = sheet.cell(3, 9).value
        pwd = sheet.cell(4, 9).value
        offer_name = sheet.cell(5, 9).value
        url_value = sheet.cell(6, 9).value
        revenue = sheet.cell(7, 9).value
        payout_for_affiliate = sheet.cell(8, 9).value

        # Navigate to URL
        anksdriver.get(url)
        anksdriver.maximize_window()

        # Login Scenario
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[1]/div/input').send_keys(uname)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[2]/div/input').send_keys(pwd)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[3]/p-checkbox/div/div[2]').click()
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[4]').click()
        time.sleep(5)

        # Create Offer
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-layout/main/div/div[2]/app-offer-list/div/div[1]/div/p-button/button/span[2]').click()
        time.sleep(5)
        anksdriver.find_element(By.XPATH, '//*[@id="p-accordiontab-0-content"]/div/div[1]/input').send_keys(offer_name)
        select_a_category = anksdriver.find_element(By.XPATH, '//*[@id="p-accordiontab-0-content"]/div/div[2]/div[1]/p-dropdown/div/div[2]')
        select_a_category.click()

        time.sleep(5)

        automotive_option=anksdriver.find_element(By.XPATH, '//*[@id="pr_id_17_list"]/p-dropdownitem[1]/li/span')

        automotive_option.click()
        time.sleep(3)

        sub_category_automotive=anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-0-content"]/div/div[2]/div[2]/p-dropdown/div/span')
        sub_category_automotive.click()
        time.sleep(2)

        motorcycle_subcategory=anksdriver.find_element(By.XPATH,'//*[@id="pr_id_18_list"]/p-dropdownitem[2]/li')
        motorcycle_subcategory.click()
        time.sleep(5)

        end_date=anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-0-content"]/div/div[3]/div[2]/p-calendar/span/button')
        end_date.click()
        time.sleep(2)

        end_date_select=anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-0-content"]/div/div[3]/div[2]/p-calendar/span/div/div/div/div[2]/table/tbody/tr[2]/td[4]/span')
        end_date_select.click()#//*[@id="p-accordiontab-0-content"]/div/div[3]/div[2]/p-calendar/span
        time.sleep(2)

        anksdriver.find_element(By.XPATH, '//*[@id="p-accordiontab-0-content"]/div/div[4]/div[1]/input').send_keys(url_value)
          

        platform_select = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-0-content"]/div/div[4]/div[2]/p-dropdown/div/span')
        platform_select.click()
        time.sleep(3)

        adjust_option = anksdriver.find_element(By.XPATH,'//*[@id="pr_id_19_list"]/p-dropdownitem[3]/li')
        adjust_option.click()
        time.sleep(3)

        advertiser_option=anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-0-content"]/div/div[5]/div[1]/p-dropdown/div/span')
        advertiser_option.click()
        time.sleep(3)

        advertiser_select= anksdriver.find_element(By.XPATH,'//*[@id="pr_id_22_list"]/p-dropdownitem/li')
        advertiser_select.click()
        time.sleep(5)

        #Advertiser_name=anksdriver.find_element(By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-add-brand/form/div[2]/input')
        #Advertiser_name.send_keys('flipkart')
        #time.sleep(3)

        #Advertiser_email= anksdriver.find_element(By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-add-brand/form/div[3]/input')
        #Advertiser_email.send_keys('newad@hh.com')
        #time.sleep(2)

        #add_advertiser = anksdriver.find_element(By.XPATH,'/html/body/p-dynamicdialog/div/div/div[2]/app-add-brand/form/div[5]/p-button/button/span')
        #add_advertiser.click()
        #time.sleep(2)
  

        specific_macros= anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-1-content"]/div/div[1]/p-inputswitch/div/span')
        specific_macros.click()
        time.sleep(3)

        affid_option= anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-1-content"]/div/div[2]/div/p-checkbox[1]/div/div[2]')
        affid_option.click()
        time.sleep(2)
  
        #country1_option = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-33-content"]/div/div[2]/div/p-checkbox[12]/div/div[2]')
        #country1_option.click()
        #time.sleep(2)
  
        clickid_option = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-1-content"]/div/div[2]/div/p-checkbox[11]/div/div[2]')
        clickid_option.click()
        time.sleep(6)

        quality_score_macros = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-1-content"]/div/div[3]/p-inputswitch/div/span')
        quality_score_macros.click()
        time.sleep(3)                                               


 
        devices=anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[1]/div[1]/p-multiselect/div')
        devices.click()
        time.sleep(5)

        mobile_select=anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[1]/div[1]/p-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[1]/li/div/div')
        mobile_select.click()
        time.sleep(3)

        desktop_select= anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[1]/div[1]/p-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[2]/li/div/div')
        desktop_select.click()
        time.sleep(3)

        tablets_select = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[1]/div[1]/p-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[3]/li/div/div')
        tablets_select.click()
        time.sleep(5)  

        operating_system = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[1]/div[2]/p-multiselect/div/div[2]/div')
        operating_system.click()
        time.sleep(5)
  
        all_for_OS = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[1]/div[2]/p-multiselect/div/p-overlay/div/div/div/div[1]/div[1]/div[2]') 
        all_for_OS.click()
        time.sleep(5)

        #all_os_of_mobile = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-18-content"]/div/div[1]/div[2]/p-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[1]/li')
        #all_os_of_mobile.click()
        #time.sleep(3)

        #all_os_of_desktop = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-18-content"]/div/div[1]/div[2]/p-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[2]/li')  
        #all_os_of_desktop.click()
        #time.sleep(3)

        #all_os_of_tablet = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-18-content"]/div/div[1]/div[2]/p-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[3]/li')
        #all_os_of_tablet.click()
        #time.sleep(3)

        region1 = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[2]/div[1]/p-multiselect/div/div[2]/div') 
        region1.click()
        time.sleep(5)

        south_asia = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[2]/div[1]/p-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[8]/li/div/div')
        south_asia.click()
        time.sleep(3)

        eastern_asia = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[2]/div[1]/p-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[6]/li/div/div')
        eastern_asia.click()
        time.sleep(3)

        countries1 = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[2]/div[2]/p-multiselect/div/div[2]/div') 
        countries1.click()
        time.sleep(5)
 
        country_india = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[2]/div[2]/p-multiselect/div/p-overlay/div/div/div/div[2]/ul/p-multiselectitem[16]/li/div/div')
        country_india.click()
        time.sleep(3)

        carriers = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[3]/div/p-multiselect/div/div[2]/div')
        carriers.click()
        time.sleep(5)

        carriers_all = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-2-content"]/div/div[3]/div/p-multiselect/div/p-overlay/div/div/div/div[1]/div[1]/div[2]')
        carriers_all.click()
        time.sleep(3)

        enable_fraud_scanning = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-3-content"]/div/div/div/p-inputswitch/div/span')
        enable_fraud_scanning.click()
        time.sleep(3)

        select_currency = anksdriver.find_element(By.XPATH,'//*[@id="p-accordiontab-4-content"]/div/div[1]/div/p-dropdown/div/span')
        select_currency.click()
        time.sleep(5)

        select_inr = anksdriver.find_element(By.XPATH,'//*[@id="pr_id_23_list"]/p-dropdownitem[1]/li')
        select_inr.click()
        time.sleep(3)
        # Set Revenue and Payout
        anksdriver.find_element(By.XPATH, '//*[@id="p-accordiontab-4-content"]/div/div[2]/div/div/input').send_keys(revenue)
        time.sleep(3)
        anksdriver.find_element(By.XPATH, '//*[@id="p-accordiontab-4-content"]/div/div[3]/div/div/input').send_keys(payout_for_affiliate)
        time.sleep(3)
        # Submit the offer
        anksdriver.find_element(By.XPATH, '//*[@id="submitButton"]/button/span').click()

        # Wait for offer creation to finish and capture the result
        time.sleep(15)  # Example wait time, adjust as necessary for your application
        result_message = "Offer is created successfully!"
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result_message = f"Offer is created successfully! at {now} "
        print(result_message)
        sheet.update_cell(2, 10, result_message)
        return result_message

    finally:
        anksdriver.quit()

if __name__ == '__main__':
    run_createoffer_club()


