#code to scrape weather.com

import requests

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

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key.
api_key = '64a6155d55401849ef48f85c95f528c7'
city_name = input("Enter the city name: ")
weather = get_weather(api_key, city_name)

if weather:
    print(f"Weather in {weather['city']}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Description: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Pressure: {weather['pressure']} hPa")
