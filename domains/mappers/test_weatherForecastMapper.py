from unittest import TestCase

from domains.values.weather_forecast import WeatherForecast
from domains.mappers.weather_forecast_mapper import WeatherForecastMapper
from infras.clients.weather_livedoor_client import WeatherLivedoorClient
from settings import CITY_CODE_KAGOSHIMA


class TestWeatherForecastMapper(TestCase):

    def test_mapper(self):

        response_body = WeatherLivedoorClient.get_city_weather(city_code=CITY_CODE_KAGOSHIMA)
        weather_forecast_mapper = WeatherForecastMapper(response_body)

        today_weather_forecast = weather_forecast_mapper.today_weather_forecast()

        # 2019/2/11 18:29時点の値
        actual_weather_forecast = WeatherForecast(
            city='鹿児島', weather='曇のち晴', min_celsius=None, max_celsius=None
        )

        self.assertEqual(today_weather_forecast, actual_weather_forecast)
