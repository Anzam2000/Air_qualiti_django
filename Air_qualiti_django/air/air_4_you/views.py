from django.shortcuts import render
import requests
from django.conf import settings


def index(request):

    WEATHER_API_KEY =  ""

    try:
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={WEATHER_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        aqi = data["list"][0]["main"]["aqi"]
        aqi_levels = {1: "Хорошо", 2: "Нормально", 3: "Умеренно", 4: "Плохо", 5: "Очень плохо"}
        return render(request, 'Air_4/index.html', {
            'aqi': aqi,
            'title': 'Качество воздуха'
        })

    except Exception as e:
        print(f"Ошибка: {e}")
        return render(request, 'Air_4/index.html', {'aqi': None, 'title': 'Ошибка'})

