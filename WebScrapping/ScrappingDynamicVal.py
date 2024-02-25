from selenium import webdriver
import time #added

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """Extract only temperature/value from text"""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    time.sleep(2) #added to load dynamic value
    element = driver.find_element(by='xpath', value="/html/body/div[1]/div/h1[2]")
    # return element.text
    return clean_text(element.text)

print(main())
