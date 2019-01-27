# coding: UTF-8
from apps.logger import AppLogger
from settings import CITY_CODE_KAGOSHIMA
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


class WeatherLivedoor:

    __BASE_URL = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'

    @staticmethod
    def get_city_weather(city_code: str) -> str:

        logger = AppLogger.get_logger(__name__)

        city_name = '鹿児島' if city_code == CITY_CODE_KAGOSHIMA else '東京'
        logger.info('%sの天気予報を取得' % city_name)

        url = WeatherLivedoor.__BASE_URL % city_code

        request = Request(url)

        body: str = ''
        try:
            with urlopen(request) as response:
                charset = response.headers.get_content_charset()
                body = response.read().decode(charset)

        except HTTPError as error:
            logger.error('Error code: %s' % error.code)

        except URLError as error:
            logger.error('Reason: %s' % error.reason)

        return body
