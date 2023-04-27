import requests
import json

print("Welcome to the Weather App!")
apiKey = "b646e6f80a604fda859120501232704"
city = input("Enter the city: ")
city = city.title()

# It was showing wrong temp for delhi so converted delhi to new delhi
if city == "Delhi":
    city = "New Delhi"

url = f"http://api.weatherapi.com/v1/current.json?key={apiKey}&q={city}"

weatherStr = requests.get(url)

weatherDict = json.loads(weatherStr.text)
weather = weatherDict["current"]["temp_c"]

print(f"The weather in {city} is {weather}°C")
