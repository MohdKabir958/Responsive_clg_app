import requests

class WeatherReport:

    def get_weather(self) ->str:

        forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
        api_key = "5a6612fa0529e69daa3e0747834c521e"
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'lat': 18.956421,
            'lon': 72.800308,
            'appid': api_key,
            'cnt':4
        }
        response = requests.get(forecast_url, params)
    
        if response.status_code == 200:

            data = response.json()
            will_rain = False
            for weather_condition in data['list']:
                condition= (weather_condition['weather'][0]['description'])
                return condition
        else:
            return response.raise_for_status()

class Quotes:
    def generate_quotes(self):
        response=requests.get('https://api.kanye.rest/')
        if response.status_code == 200:
            data = response.json()
            quote = data['quote']
            return quote

