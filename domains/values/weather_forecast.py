# coding: UTF-8

from dataclasses import dataclass


@dataclass(frozen=True)
class WeatherForecast:

    city: str
    weather: str
    max_celsius: int or None
    min_celsius: int or None
