
# main_script.py

import datetime
from config import initialize_sheets, get_webdriver, By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_login_club():
    anksdriver = None  # Initialize driver to None to handle cases where get_webdriver() might fail
    try:
        # Initialize Google Sheets
        sheet = initialize_sheets()
        
        # Attempt to get the WebDriver
        anksdriver = get_webdriver()

        # Fetch credentials and URL
        url = sheet.cell(1, 1).value
        username = sheet.cell(2, 1).value
        password = sheet.cell(3, 1).value

        # Start WebDriver and open URL
        anksdriver.get(url)
        anksdriver.implicitly_wait(5) 
        print("Navigated to:", url)

        # Login operation with explicit waits and handling
        try:
            WebDriverWait(anksdriver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[1]/div/input'))).send_keys(username)
            WebDriverWait(anksdriver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[2]/div/input'))).send_keys(password)
            anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[3]/p-checkbox/div/div[2]').click()
            anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[4]').click()

            # Check for error messages specifically after attempting to log in
            try:
                error_message = WebDriverWait(anksdriver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-class")))
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print("Login failed with error:", error_message.text)
                sheet.update_cell(1, 2, f"Login failed at {now}: " + error_message.text)
                return f"Login failed at {now}: " + error_message.text
            except TimeoutException:
                print("No error message detected, proceeding to verify login success.")
            
            # Verification of successful login
            WebDriverWait(anksdriver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[1]/li[2]/div[1]/a/span')))
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            sheet.update_cell(1, 2, f"Login successfully at {now}")
            print(f"Login successful at {now}, and data updated in Google Sheet.")

        except TimeoutException as e:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("Login operation timed out:", str(e))
            sheet.update_cell(1, 2, f"Login failed due to timeout at {now}")
            return f"Login operation timed out at {now}."

    except NoSuchElementException as e:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("Element not found during login operation:", str(e))
        sheet.update_cell(1, 2, f"Login failed due to missing element at {now}")
        return f"Login failed due to missing element at {now}."
    except Exception as e:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("An error occurred:", str(e))
        return f"An error occurred during the script execution at {now}."
    finally:
        if anksdriver:
            anksdriver.quit()
            print("WebDriver session closed.")

    return "Python script executed successfully and result written to Google Sheet!"

if __name__ == "__main__":
    result = run_login_club()
    print(result)
