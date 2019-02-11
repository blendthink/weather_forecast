# coding: UTF-8

import json
from domains.entities.weather_forecast import WeatherForecast


class WeatherForecastMapper:

    __LOCATION = 'location'
    __CITY = 'city'
    __LINK = 'link'
    __FORECASTS = 'forecasts'

    __TELOP = 'telop'
    __TEMPERATURE = 'temperature'
    __MAX = 'max'
    __MIN = 'min'
    __CELSIUS = 'celsius'

    weather_forecast_json: json

    def __init__(self, weather_forecast_json_text: str):
        self.weather_forecast_json = json.loads(weather_forecast_json_text)

    def today_weather_forecast(self) -> WeatherForecast or None:

        if self.weather_forecast_json is None:
            return None

        if self.__LOCATION not in self.weather_forecast_json:
            return None

        location = self.weather_forecast_json[self.__LOCATION]
        if location is None:
            return None

        if self.__CITY not in location:
            return None

        city = location[self.__CITY]
        if city is None:
            return None

        if self.__FORECASTS not in self.weather_forecast_json:
            return None

        forecasts: list = self.weather_forecast_json[self.__FORECASTS]
        if forecasts is None or len(forecasts) == 0:
            return None

        today_forecast = forecasts[0]
        if today_forecast is None:
            return None

        if self.__TELOP not in today_forecast:
            return None

        weather = today_forecast[self.__TELOP]
        if weather is None:
            return None

        max_celsius = None
        min_celsius = None
        if self.__TEMPERATURE in today_forecast:
            temperature = today_forecast[self.__TEMPERATURE]
            if self.__MIN in temperature:
                min_temperature = temperature[self.__MIN]
                if min_temperature is not None and self.__CELSIUS in min_temperature:
                    min_celsius = min_temperature[self.__CELSIUS]

            if self.__MAX in temperature:
                max_temperature = temperature[self.__MAX]
                if max_temperature is not None and self.__CELSIUS in max_temperature:
                    max_celsius = max_temperature[self.__CELSIUS]

        return WeatherForecast(
            city=city, weather=weather, min_celsius=min_celsius, max_celsius=max_celsius
        )
