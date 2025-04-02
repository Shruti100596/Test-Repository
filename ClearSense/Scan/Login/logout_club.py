def run_logout():
    import time
    import os
    import json
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    anksdriver = webdriver.Chrome()
    actions = ActionChains(anksdriver)

    #with open("config.json", "r") as jsonfile:
    #    cdata = json.load(jsonfile)

    #set session name
    #anksdriver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "TC18/Desktop/ValidUsername/ValidPassword/Successful-Login-Scenario"}}')

    anksdriver.get("https://sfolkar.cleartrust.club")
    time.sleep(5)
    #login and passwords keys
    anksdriver.maximize_window()

    uname = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[1]/div/input')
    uname.send_keys('gpx8nc3vh1@sfolkar.com')
    time.sleep(2)
    pwd = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[2]/div/input')
    pwd.send_keys('Gpx8nc3vh1@123')
    time.sleep(2)

    tick_box=anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[3]/p-checkbox/div/div[2]')
    tick_box.click()
    time.sleep(3)

    enter = anksdriver.find_element(By.XPATH, '/html/body/app-root/app-login/div/div/div/div[1]/div/form/div[4]')
    enter.click()
    time.sleep(3)

    logout_button=anksdriver.find_element(By.XPATH,'/html/body/app-root/app-layout/main/aside/app-aside-menu/div/ul[2]/li[3]/a/span')
    logout_button.click()
    time.sleep(3)
    
    anksdriver.maximize_window()

    return "Python script executed successfully!"
    anksdriver.quit()
