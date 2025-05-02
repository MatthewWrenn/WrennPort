from bs4 import BeautifulSoup
import requests
import csv
#takes user input and runs data validation to check that its 3 characters and that they are letters.
def user_input():
    print("Currency exchange rate checker please use valid 3 character currency codes.")
    while True:
        Currency1 = input("Please enter the first currency: ").upper()
        if len(Currency1) != 3 or not Currency1.isalpha():
            print("Please enter a valid 3 character currency.")
            continue
        Currency2 = input("Please enter the second currency: ").upper()
        if len(Currency2) != 3 or not Currency2.isalpha():
            print("Please enter a valid 3 character currency.")
            continue
        if Currency1 == Currency2:
            print("Please enter two different currencies.")
            continue
        #opens the file in read mode reads the CSV and puts in a set compares the set against the 2 currency varibles and breaks if they match meaning the currency code is valid.
        with open("currency.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            # Check if both currency codes are listed in the CSV file
            matched_currencies = {row[0] for row in reader}
            if Currency1 in matched_currencies and Currency2 in matched_currencies:
                return Currency1, Currency2  # Break the loop and return valid inputs
            else:
                #prints an error if the codes given don't match those in the set
                print("Invalid currency codes.")
                continue
#uses BeautifulSoup to create a useble url for the exhchange rates provided by the user in user input.
def get_currency(Currency1, Currency2): #defines the currency varibles as parameters for this function.
    url = f"https://www.x-rates.com/calculator/?from={Currency1}&to={Currency2}&amount=1" #creates a varible containing the url we wish to parse.
    content = requests.get(url).text #gets the sites souce code as text
    mySoup = BeautifulSoup(content, 'html.parser')#creates a varible that contains the html parser
    rate = mySoup.find("span", class_="ccOutputRslt").getText()#fills the rate varible the text from the exchnage rate box on the website
    rate = float(rate[:4]) #Parses off text the currency code text
    rate = round(rate, 3) #rounds the float is that bad for currecy exhange?
    return rate

Currency1, Currency2 = user_input() #calls user inupt to populate the currency varibles
rate = get_currency(Currency1, Currency2) #populates a seperate rate varbile for text concatenation from the get_currency function 
print(f"The exchange rate from {Currency1} to {Currency2} is {rate}.") #text concatenation
