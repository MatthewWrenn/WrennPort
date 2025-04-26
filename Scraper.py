from selenium import webdriver
#set up my function to get the webdriver
def get_driver():
    #set my webdriver options
    opt = webdriver.ChromeOptions()
    opt.add_argument("disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("no-sandbox")
    opt.add_argument("disable-blink-features=AutomationControlled")
    opt.add_experimental_option("excludeSwitches", ["enable-automation"])
    #set up my webdriver instance
    driver = webdriver.Chrome(options=opt)
    driver.get("http://automated.pythonanywhere.com/")
    return driver


def main():
    #call the get_driver function
    driver = get_driver()
    #getting Xpath for the element
    element = driver.find_element("xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())