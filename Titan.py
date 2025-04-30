import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#set up my function to get the webdriver
def get_driver():
    #set my webdriver options
    try:
        print("starting up the webdriver...")
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False}) #disables password manager for login automation puurposes
        opt.add_argument("disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("no-sandbox")
        opt.add_argument("disable-blink-features=AutomationControlled")
        opt.add_experimental_option("excludeSwitches", ["enable-automation"])
        opt.add_argument("--log-level=3") 
        service = Service("C:\\Users\\Matt\\Web_Driver\\chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=opt)
        print("webdriver initialized successfully.")
        driver.get("https://titan22.com/account/register?checkout_url=https%3A%2F%2Ftitan22.com%2F")
        print("website loaded successfully.")
        return driver
    except Exception as e:
        print(f"An error occurred while starting up the webdriver: {e}")
        raise

try:
  #call the get_driver function
   driver = get_driver()
   wait = WebDriverWait(driver, 30)
   wait.until(EC.presence_of_element_located((By.ID, "FirstName"))).send_keys("John") #Puts your first Name in the First Name field
   driver.find_element(By.ID, "LastName").send_keys("Doh") #Puts your last name in the Last Name field
   driver.find_element(By.ID, "Email").send_keys("tonot85192@mongrec.com") #generate an email and use it here for your account
   driver.find_element(By.ID, "CreatePassword").send_keys("test2061") #pick a password and use it here for your account
   driver.find_element(By.ID, "customer[accepts_terms]").click() #clicks the terms and conditions checkbox
   driver.find_element(By.XPATH, "/html/body/main/article/section/div/form/button").send_keys(Keys.RETURN) #clicks the create account button
   wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/div[1]/div/div[2]/nav[1]/ul/li[2]/a"))).click() #clicks shop all on the home page.
   wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/article/div/div/div/div[1]/section/div[3]/div[7]/div/a/div[1]/div[1]/div/div/div/div[2]/div/img"))).click() #selects a pair of shoes to buy
   wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/article/div[1]/section[1]/div/div[2]/form/div/div/ul/li[8]/label"))).click() #selects size 11 my own size
   driver.find_element(By.XPATH, "/html/body/main/article/div[1]/section[1]/div/div[2]/form/button").send_keys(Keys.RETURN) #clicks the add to cart button
   time.sleep(5) #waits so you can see that it added to the cart
finally:
  #close the driver
  driver.quit()
  print("WebDriver closed.")
