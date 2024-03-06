import requests
import csv
from datetime import datetime

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit/'metric' for Celsius.
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        weather = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity'],
            'pressure': weather_data['main']['pressure'],
            'icon': weather_data['weather'][0]['icon']
        }
        return weather
    else:
        print(f"Error: {response.status_code}")
        return None

def write_to_csv(weather_data, filename="weather_data.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['City', 'Temperature', 'Description', 'Humidity', 'Pressure', 'Icon', 'Timestamp'])
        writer.writerow([
            weather_data['city'],
            weather_data['temperature'],
            weather_data['description'],
            weather_data['humidity'],
            weather_data['pressure'],
            weather_data['icon'],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key.
api_key = '64a6155d55401849ef48f85c95f528c7'
city_name = input("Enter the city name: ")
weather = get_weather(api_key, city_name)

if weather:
    write_to_csv(weather)
    print(f"Weather data for {weather['city']} has been written to weather_data.csv.")
