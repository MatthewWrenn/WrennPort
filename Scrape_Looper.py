import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import keyboard
import time

#function to check for enter key press this function is threaded
stop = False #setting it to false so the while loop won't trigger and break the for loop below.
def check_keys():
    global stop #using global so I can change the value of stop in the function
    print("Press Enter to exit the loop.")
    while not stop: #while stop == false it will listening for the enter press
        if keyboard.is_pressed("enter"):  
            print("Enter key pressed. Ignoring further key presses.")
            stop = True  
            break #breaks the loop so you can't reset the stop variable to false again
#set up my function to get the webdriver
def get_driver():
    #WebDriver Path
    WebDPath  = "C:\\Users\\Matt\\Web_Driver\\chromedriver.exe"
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
        service = Service(WebDPath)
        driver = webdriver.Chrome(service=service, options=opt) #creating the webdriver
        print("webdriver initialized successfully.")
        driver.get("http://automated.pythonanywhere.com/") #loading the website
        print("website loaded successfully.")
        return driver
    except Exception as e:
        print(f"An error occurred while starting up the webdriver: {e}")
        raise

def split_text(text):
    #Split the text  after the  ": "
    output = float(text.split(": ")[1])
    return output

#This is a second WebDriver that loads a headless browser that plays the Cowboy Bebop theme song from the internt archive.
WebDPath  = "C:\\Users\\Matt\\Web_Driver\\chromedriver.exe"
opt = webdriver.ChromeOptions()
opt.add_argument("disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("no-sandbox")
opt.add_argument("headless")
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_argument("--log-level=3") 
service = Service(WebDPath)
driver2 = webdriver.Chrome(service=service, options=opt)
print("webdriver2 initialized successfully.")
driver2.get("https://archive.org/details/tvtunes_10883")
element = driver2.find_element("id", value="jw6").send_keys(Keys.RETURN)
print("website2 loaded successfully.")

key_thread = threading.Thread(target=check_keys, daemon=True)
key_thread.start()

for i in range(1, 51):
    if stop:
        break
    try:
        #call the get_driver function
        driver = get_driver()
        time.sleep(2)
        #getting Xpath for the element
        element2 =  driver.find_element("xpath", value="/html/body/div[1]/div/h1[2]")
        value = split_text(element2.text) #calling the split_text function
        currentDateTime = datetime.now().strftime("%m-%d-%Y_%H-%M-%S") #getting my current date and time for the txt file
        filename = f"{currentDateTime}.txt" #creating and f string variable for the filename
        with open(filename, 'w') as f:
            f.write(f'{value}') #writing the scraped to the file
            print(f"File {i} created: {value} written to {filename}")
    finally:
        #close the driver
        driver.quit()
        print("WebDriver closed.")
else:
    driver2.quit()
    print("Exitng...")
