from calendar import c
from bs4 import BeautifulSoup
import requests
import csv

def user_input():
    print("Currency converter please use valid 3 character currency codes.")
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
        #opens the file in read mode
        with open("currency.csv", 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            # Check if both currency codes are listed in the CSV file
            matched_currencies = {row[0] for row in reader}
            if Currency1 in matched_currencies and Currency2 in matched_currencies:
                return Currency1, Currency2  # Break the loop and return valid inputs
            else:
                print("Invalid currency codes.")
                continue
user_input()
def get_currency(Currency1, Currency2):
    url = f"https://www.x-rates.com/calculator/?from={Currency1}&to={Currency2}&amount=1"
    content = requests.get(url).text
    mySoup = BeautifulSoup(content, 'html.parser')
    rate = mySoup.find("span", class_="ccOutputRslt").getText()
    rate = float(rate[:4])
    rate = round(rate, 2)
    return rate

Currency1, Currency2 = user_input()
rate = get_currency(Currency1, Currency2)
print(f"The exchange rate from {Currency1} to {Currency2} is {rate}.")