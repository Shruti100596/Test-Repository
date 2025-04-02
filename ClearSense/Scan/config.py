# config.py

import time
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains

#def initialize_sheets():
#    scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
#    creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/shrutikamble/Desktop/Shruti/my-automation-project-422111-1697f8b35987.json', scope)
#    client = gspread.authorize(creds)
#    sheet = client.open('QA_Setup_club').sheet1
#    return sheet

#def get_webdriver():
#    anksdriver = webdriver.Chrome()
#    anksdriver.maximize_window()
#    return anksdriver
import os
import datetime
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def initialize_sheets(sheet_name='QA_Automation_Script'):
    try:
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds_path = os.getenv('GOOGLE_CREDS_PATH', '/Users/shrutikamble/Desktop/Shruti/my-automation-project-422111-1697f8b35987.json')
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        client = gspread.authorize(creds)
        sheet = client.open(sheet_name).sheet1
        return sheet
    except Exception as e:
        logging.error(f"Failed to initialize Google Sheets: {e}")
        raise

def get_webdriver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        anksdriver = webdriver.Chrome(options=options)
        return anksdriver
    except Exception as e:
        logging.error(f"Failed to initialize WebDriver: {e}")
        raise

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    sheet = initialize_sheets()
    driver = get_webdriver()
    logging.info("Google Sheet and WebDriver have been initialized successfully.")

