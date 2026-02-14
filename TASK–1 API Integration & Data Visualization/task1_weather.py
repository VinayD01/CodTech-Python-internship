import requests
import matplotlib.pyplot as plt

API_KEY = "5a5842965e7b35024118cdfab32a96f9"
cities = ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad"]

URL = "https://api.openweathermap.org/data/2.5/weather"

valid_cities = []
temperatures = []

for city in cities:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(URL, params=params)
    data = response.json()

    if response.status_code == 200:
        valid_cities.append(city)
        temperatures.append(data["main"]["temp"])
    else:
        print(f"Failed for {city}: {data.get('message')}")

plt.bar(valid_cities, temperatures)
plt.title("Temperature Comparison Across Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")
plt.show()
