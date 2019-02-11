# coding: UTF-8

from domains.mappers.weather_forecast_mapper import WeatherForecastMapper
from infras.clients.weather_livedoor_client import WeatherLivedoorClient
from infras.clients.slack_client import SlackClient
from settings import CITY_CODE_KAGOSHIMA, CITY_CODE_TOKYO, WEB_HOOK_URL

kagoshima_weather_forecast = WeatherLivedoorClient.get_city_weather(city_code=CITY_CODE_KAGOSHIMA)
kagoshima_weather_forecast_mapper = WeatherForecastMapper(kagoshima_weather_forecast)

kagoshima_today_weather_forecast = kagoshima_weather_forecast_mapper.today_weather_forecast()
if kagoshima_today_weather_forecast is None:
    kagoshima_message = '鹿児島の天気情報はありません。'
else:
    kagoshima_message = '%sの天気 %s\n' % (
        kagoshima_today_weather_forecast.city,
        kagoshima_today_weather_forecast.weather
    )
    kagoshima_message += kagoshima_today_weather_forecast.get_celsius()

tokyo_weather_forecast = WeatherLivedoorClient.get_city_weather(city_code=CITY_CODE_TOKYO)
tokyo_weather_forecast_mapper = WeatherForecastMapper(tokyo_weather_forecast)

tokyo_today_weather_forecast = tokyo_weather_forecast_mapper.today_weather_forecast()
if tokyo_today_weather_forecast is None:
    tokyo_message = '東京の天気情報はありません。'
else:
    tokyo_message = '%sの天気 %s\n' % (
        tokyo_today_weather_forecast.city,
        tokyo_today_weather_forecast.weather
    )
    tokyo_message += tokyo_today_weather_forecast.get_celsius()

message = '<@kagoshimastaffs> <@tokyostaffs> ヤン坊マー坊天気予報 :notes:'
message += '\n\n'
message += '<@kagoshimastaffs> ぼくの名前はヤン坊 :musical_note:'
message += '\n\n'
message += kagoshima_message
message += '\n\n'
message += '<@tokyostaffs> ぼくの名前はマー坊 :musical_note:'
message += '\n\n'
message += tokyo_message
message += '\n\n'
message += '<@kagoshimastaffs> <@tokyostaffs> ２人合わせて ヤンマーだ :musical_note:\n'
message += '君と僕とでヤンマーだ :musical_note:'

slack_client = SlackClient(WEB_HOOK_URL)
slack_client.post(message)
