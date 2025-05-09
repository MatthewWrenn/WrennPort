from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
#set up my function to get the webdriver
def get_driver():
    #set my webdriver options
    try:
        print("Starting up the webdriver...")
        opt = webdriver.ChromeOptions()
        opt.add_argument("disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("no-sandbox")
        opt.add_argument("disable-blink-features=AutomationControlled")
        opt.add_experimental_option("excludeSwitches", ["enable-automation"])
        opt.add_argument("--log-level=3") 
        service = Service("C:\\Users\\Matt\\Web_Driver\\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=opt)
        print("WebDriver initialized successfully.")
        driver.get("http://automated.pythonanywhere.com/")
        print("Website loaded successfully.")
        return driver
    except Exception as e:
        print(f"An error occurred while initializing the WebDriver: {e}")
        raise

def split_text(text):
    #Split the text  after the  ": "
    output = float(text.split(": ")[1])
    return output

def main():
  try:
    #call the get_driver function
    driver = get_driver()
    time.sleep(2)
    #getting Xpath for the element
    element = driver.find_element("xpath", value="/html/body/div[1]/div/h1[1]")
    element2 =  driver.find_element("xpath", value="/html/body/div[1]/div/h1[2]")
    value = split_text(element2.text)
    return f"{element.text}\n{value}"
  finally:
    #close the driver
    driver.quit()
    print("WebDriver closed.")

try:
    print(main())
except Exception as e:
    print(f"An error occurred: {e}")