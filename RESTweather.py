import requests

r = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=Seattle,US,WA&appid=8177c55ec4161a04f9b279b5ec254432&units=imperial")
content  = r.json()

temp = content["list"][0]["main"]["temp"]
feels_like = content["list"][0]["main"]["feels_like"]
temp_min = content["list"][0]["main"]["temp_min"]
temp_max = content["list"][0]["main"]["temp_max"]
print(f"Seattle Weather: \nTemp: {temp}\nFeels like: {feels_like}\nMin Temp: {temp_min}\nMax Temp: {temp_max}")