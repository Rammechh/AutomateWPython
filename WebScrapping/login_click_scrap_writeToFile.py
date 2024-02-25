from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Enter key to login
import time
from datetime import datetime as dt 

def get_drvier():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options = options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    """Extract only temperature/value from text"""
    output = float(text.split(": ")[1])
    return output

def write_file(text):
    filepath = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    filepath = "files/webscrap/scrap" + filepath
    with open(filepath, 'w') as file:
        file.write(text)

def main():
    driver = get_drvier()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN) #Enter key
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
    for i in range(10):
        time.sleep(2)
        text = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
        tempText = str(clean_text(text))
        write_file(tempText)

print(main())