from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
#set up my function to get the webdriver
def get_driver():
    #set my webdriver options
    try:
        print("Starting up the webdriver...")
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False}) #disables password manager for login automation puurposes
        opt.add_argument("disable-infobars") #disables info bars
        opt.add_argument("start-maximized") #maximizes the window
        opt.add_argument("no-sandbox") #disables the sandbox
        opt.add_argument("disable-blink-features=AutomationControlled") #disables the blink features
        opt.add_experimental_option("excludeSwitches", ["enable-automation"]) #excludes the automation switches
        opt.add_argument("--log-level=3") #disables logging at the level 3 to supprse a known error
        service = Service("C:\\Users\\Matt\\Web_Driver\\chromedriver.exe") #path to the chromedriver
        driver = webdriver.Chrome(service=service, options=opt)
        print("WebDriver initialized successfully.")
        driver.get("http://automated.pythonanywhere.com/login/")
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
    #getting Xpath for the element
    driver.find_element("id", value="id_username").send_keys("automated") #types in the username
    time.sleep(2)
    driver.find_element("id", value="id_password").send_keys("automatedautomated" + Keys.RETURN) #types in the password and hits enter
    time.sleep(2)
    driver.find_element("xpath", value="/html/body/nav/div/a").click() #clicks the link to go to the main page
    time.sleep(3)
    #getting Xpath for the element
    element = driver.find_element("xpath", value="/html/body/div[1]/div/h1[1]")
    element2 =  driver.find_element("xpath", value="/html/body/div[1]/div/h1[2]")
    value = split_text(element2.text) #scrapes annd sends to text to print in the main function call
    return f"{element.text}\n{value}"
  finally:
    #close the driver
    driver.quit()
    print("WebDriver closed.")

try:
    print(main())
except Exception as e:
    print(f"An error occurred: {e}")
