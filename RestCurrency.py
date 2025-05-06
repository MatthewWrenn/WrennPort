from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

# Scrapes the currency exchange rate from the website uses BeautifulSoup to parse the HTML to get the vaule  needed
def get_currency(Currency1, Currency2):
    url = f"https://www.x-rates.com/calculator/?from={Currency1}&to={Currency2}&amount=1"
    content = requests.get(url).text
    mySoup = BeautifulSoup(content, 'html.parser')
    rate = mySoup.find("span", class_="ccOutputRslt").getText()
    rate = float(rate[:4])
    rate = round(rate, 2)
    return rate

#createing an flask for my api
app = Flask(__name__)

@app.route('/')
def home():
    return  "<h1>Hello Welcome to Currency Exhchage Rates</h1> <p>api/v1/usd-eur</p>"
    
#sets up the url in  our flask api for an input and output currency
@app.route('/api/v1/<in_cur>-<out_cur>')
#This fuction creates the json for for api to be queried
def api(in_cur, out_cur):
    rate = get_currency(in_cur, out_cur)
    dictionary = {"Input Currency":in_cur,"Output Currency":out_cur,"Rate":rate}
    return jsonify(dictionary) #returns the json for the api

if __name__ == '__main__': #ensures the api is not run when imported as module
    app.run()