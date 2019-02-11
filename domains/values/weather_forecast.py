# coding: UTF-8

from dataclasses import dataclass


@dataclass(frozen=True)
class WeatherForecast:

    city: str
    weather: str
    max_celsius: int or None
    min_celsius: int or None

    def __get_min_celsius(self)->str:

        if self.min_celsius is None:
            return '最低気温情報なし'

        return '最低気温は%s℃' % self.min_celsius

    def __get_max_celsius(self)->str:

        if self.max_celsius is None:
            return '最高気温情報なし'

        return '最高気温は%s℃' % self.max_celsius

    def get_celsius(self)->str:
        if self.max_celsius is self.min_celsius is None:
            return '気温情報なし'

        return '%s %s' % (self.__get_min_celsius(), self.__get_max_celsius())
