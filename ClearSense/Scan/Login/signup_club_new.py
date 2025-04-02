from config import get_webdriver, initialize_sheets
from selenium.webdriver.common.by import By
import time
import datetime  # Import datetime to use for timestamps
from selenium.common.exceptions import NoSuchElementException

def run_signup1():
    # Initialize Google Sheets
    sheet = initialize_sheets()

    # Fetch credentials and URL from Google Sheet
    business_name = sheet.cell(2, 3).value
    email_id = sheet.cell(3, 3).value
    password_1 = sheet.cell(4, 3).value

    # Initialize WebDriver from config
    anksdriver = get_webdriver()

    try:
        # Navigate to the signup page
        anksdriver.get("https://cleartrust.club")
        time.sleep(2)  # Wait for the page to load
        create_an_account = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[5]/p/a')
        create_an_account.click()
        time.sleep(2)

        # Automate form submission
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[1]/input').send_keys(business_name)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[2]/input').send_keys(email_id)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[3]/div/p-radiobutton[1]/div/div[2]/span').click()
        time.sleep(2)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[4]/div/input').send_keys(password_1)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[4]/div/i').click()
        time.sleep(2)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[5]/div/input').send_keys(password_1)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[5]/div/i').click()
        time.sleep(2)
        anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[6]/p-checkbox/div/div[2]').click()
        submit_button = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[7]')
        submit_button.click()
        time.sleep(2)

        # Check for error message
        try:
            error_message = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-register/div/div/div/div[1]/div/form/div[7]/p-toast/div/p-toastitem/div/div/div/div[2]').text
            print(error_message)
            if "Business already exists with this email id. Plz check" in error_message:
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                message = f"Account already exists error at {now}."
                print(message)
                #print(email_id)
                #domain_name = email_id.split('@')[-1].split('.')[0]
                #dynamic_url = f"https://{domain_name}.cleartrust.club"
                #print(dynamic_url)
                #anksdriver.get(dynamic_url)
                #anksdriver.maximize_window()
                #time.sleep(10)
                sheet.update_cell(2, 4, message)
                return message
        except NoSuchElementException:
            # If no error message, proceed with login
            pass

        # Proceed with dynamic URL and login
        print(email_id)
        domain_name = email_id.split('@')[-1].split('.')[0]
        dynamic_url = f"https://{domain_name}.cleartrust.club"
        print(dynamic_url)
        anksdriver.implicitly_wait(5) 
        anksdriver.get(dynamic_url)
        anksdriver.maximize_window()
        
                                                               
        # Login sequence
        login_name_field = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[1]/div/input')
        login_name_field.send_keys(email_id)
        time.sleep(2)
        login_password_field = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[2]/div/input')
        login_password_field.send_keys(password_1)
        time.sleep(2)
        remember_me_checkbox = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[3]/p-checkbox/div/div[2]')
        remember_me_checkbox.click()
        login_button = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[4]')
        login_button.click()
        time.sleep(5)

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        result_message = f"Signup and login completed successfully at {now}"
        sheet.update_cell(2, 4, result_message)
        print(result_message)

    except Exception as e:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        error_message = f"An error occurred at {now}: {str(e)}"
        print(error_message)
        sheet.update_cell(2, 4, error_message)
        return error_message

    finally:
        # Ensure the driver quits after operations
        if anksdriver:
            anksdriver.quit()

    return "Signup process completed. Please check the Google Sheet for details."

if __name__ == "__main__":
    result = run_signup1()
    print(result)
