from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import time
#set up my function to get the webdriver
def get_driver():
    #set my webdriver options
    try:
        print("starting up the webdriver...")
        opt = webdriver.ChromeOptions()
        opt.add_argument("disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("no-sandbox")
        opt.add_argument("disable-blink-features=AutomationControlled")
        opt.add_experimental_option("excludeSwitches", ["enable-automation"])
        opt.add_argument("--log-level=3") 
        service = Service("C:\\Users\\Matt\\Web_Driver\\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=opt)
        print("webdriver initialized successfully.")
        driver.get("http://automated.pythonanywhere.com/")
        print("website loaded successfully.")
        return driver
    except Exception as e:
        print(f"An error occurred while starting up the webdriver: {e}")
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
    element2 =  driver.find_element("xpath", value="/html/body/div[1]/div/h1[2]")
    value = split_text(element2.text)
    currentDateTime = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
    filename = f"{currentDateTime}.txt"
    with open(filename, 'w') as f:
        f.write(f'{value}\n')
        return filename
  finally:
    #close the driver
    driver.quit()
    print("WebDriver closed.")

try:
    print(main())
except Exception as e:
    print(f"an error occurred: {e}")
