from unittest import TestCase
from infras.weather_livedoor import WeatherLivedoor
from settings import CITY_CODE_KAGOSHIMA


class TestWeatherLivedoor(TestCase):

    def test_get_city_weather(self):

        # 1/28でのテスト
        kagoshima_weather_forecast = (b'{"pinpointLocations":[{"link":"http://weather.livedoor.com/area/forecast/462'
 b'0100","name":"\\u9e7f\\u5150\\u5cf6\\u5e02"},{"link":"http://weather.livedoo'
 b'r.com/area/forecast/4620400","name":"\\u6795\\u5d0e\\u5e02"},{"link":"http:'
 b'//weather.livedoor.com/area/forecast/4620600","name":"\\u963f\\u4e45\\u6839'
 b'\\u5e02"},{"link":"http://weather.livedoor.com/area/forecast/4620800","na'
 b'me":"\\u51fa\\u6c34\\u5e02"},{"link":"http://weather.livedoor.com/area/fore'
 b'cast/4621000","name":"\\u6307\\u5bbf\\u5e02"},{"link":"http://weather.lived'
 b'oor.com/area/forecast/4621501","name":"\\u85a9\\u6469\\u5ddd\\u5185\\u5e0'
 b'2"},{"link":"http://weather.livedoor.com/area/forecast/4621502","name":"'
 b'\\u85a9\\u6469\\u5ddd\\u5185\\u5e02\\u7511\\u5cf6"},{"link":"http://weather'
 b'.livedoor.com/area/forecast/4621600","name":"\\u65e5\\u7f6e\\u5e02"},{"link'
 b'":"http://weather.livedoor.com/area/forecast/4621800","name":"\\u9727\\u5c'
 b'f6\\u5e02"},{"link":"http://weather.livedoor.com/area/forecast/4621900","'
 b'name":"\\u3044\\u3061\\u304d\\u4e32\\u6728\\u91ce\\u5e02"},{"link":"http://'
 b'weather.livedoor.com/area/forecast/4622000","name":"\\u5357\\u3055\\u3064\\u'
 b'307e\\u5e02"},{"link":"http://weather.livedoor.com/area/forecast/4622300"'
 b',"name":"\\u5357\\u4e5d\\u5dde\\u5e02"},{"link":"http://weather.livedoor.com'
 b'/area/forecast/4622400","name":"\\u4f0a\\u4f50\\u5e02"},{"link":"http://wea'
 b'ther.livedoor.com/area/forecast/4622500","name":"\\u59f6\\u826f\\u5e02"},{"'
 b'link":"http://weather.livedoor.com/area/forecast/4639200","name":"\\u3055'
 b'\\u3064\\u307e\\u753a"},{"link":"http://weather.livedoor.com/area/forecast/'
 b'4640400","name":"\\u9577\\u5cf6\\u753a"},{"link":"http://weather.livedoor.c'
 b'om/area/forecast/4645200","name":"\\u6e67\\u6c34\\u753a"}],"link":"http://w'
 b'eather.livedoor.com/area/forecast/460010","forecasts":[{"dateLabel":"\\u4'
 b'eca\\u65e5","telop":"\\u66c7\\u6642\\u3005\\u6674","date":"2019-01-28","t'
 b'emperature":{"min":null,"max":{"celsius":"15","fahrenheit":"59.0"}},"image":'
 b'{"width":50,"url":"http://weather.livedoor.com/img/icon/9.gif","title":"'
 b'\\u66c7\\u6642\\u3005\\u6674","height":31}},{"dateLabel":"\\u660e\\u65e5",'
 b'"telop":"\\u6674\\u308c","date":"2019-01-29","temperature":{"min":{"celsiu'
 b's":"3","fahrenheit":"37.4"},"max":{"celsius":"14","fahrenheit":"57.2"}},"ima'
 b'ge":{"width":50,"url":"http://weather.livedoor.com/img/icon/1.gif","title":"'
 b'\\u6674\\u308c","height":31}}],"location":{"city":"\\u9e7f\\u5150\\u5cf6"'
 b',"area":"\\u4e5d\\u5dde","prefecture":"\\u9e7f\\u5150\\u5cf6\\u770c"},"pub'
 b'licTime":"2019-01-28T05:00:00\\u002b0900","copyright":{"provider":[{"link'
 b'":"http://tenki.jp/","name":"\\u65e5\\u672c\\u6c17\\u8c61\\u5354\\u4f1a"}]'
 b',"link":"http://weather.livedoor.com/","title":"(C) LINE Corporation","image'
 b'":{"width":118,"link":"http://weather.livedoor.com/","url":"http://weather.l'
 b'ivedoor.com/img/cmn/livedoor.gif","title":"livedoor \\u5929\\u6c17\\u60c5\\u'
 b'5831","height":26}},"title":"\\u9e7f\\u5150\\u5cf6\\u770c \\u9e7f\\u5150\\u'
 b'5cf6 \\u306e\\u5929\\u6c17","description":{"text":" \\u4e5d\\u5dde\\u5357\\'
 b'u90e8\\u306f\\u3001\\u6674\\u308c\\u3084\\u66c7\\u308a\\u3068\\u306a\\u306'
 b'3\\u3066\\u3044\\u307e\\u3059\\u3002\\n \\u5944\\u7f8e\\u5730\\u65b9\\u306f'
 b'\\u3001\\u6674\\u308c\\u3066\\u3044\\u307e\\u3059\\u3002\\n\\n \\u4e5d\\u5dd'
 b'e\\u5357\\u90e8\\u306f\\u300128\\u65e5\\u306f\\u6c17\\u5727\\u306e\\u8c37\\'
 b'u3084\\u6e7f\\u3063\\u305f\\u7a7a\\u6c17\\u306e\\u5f71\\u97ff\\u3092\\u53d'
 b'7\\u3051\\u308b\\u3067\\u3057\\u3087\\u3046\\u30022\\n9\\u65e5\\u306f\\u9ad'
 b'8\\u6c17\\u5727\\u306b\\u8986\\u308f\\u308c\\u308b\\u898b\\u8fbc\\u307f\\u3'
 b'067\\u3059\\u3002\\n \\u5944\\u7f8e\\u5730\\u65b9\\u306f\\u300128\\u65e5\\u'
 b'304b\\u308929\\u65e5\\u306b\\u304b\\u3051\\u3066\\u6c17\\u5727\\u306e\\u8c'
 b'37\\u3084\\u6e7f\\u3063\\u305f\\u7a7a\\u6c17\\u306e\\u5f71\\u97ff\\u3092\\u'
 b'53d7\\n\\u3051\\u308b\\u3067\\u3057\\u3087\\u3046\\u3002\\n\\n \\u4e5d\\u5dd'
 b'e\\u5357\\u90e8\\u3067\\u306f\\u300128\\u65e5\\u306f\\u6982\\u306d\\u66c7\\'
 b'u308a\\u3067\\u96e8\\u306e\\u964d\\u308b\\u6240\\u304c\\u3042\\u308a\\u307'
 b'e\\u3059\\u304c\\u3001\\u671d\\u6669\\u306f\\u6674\\u308c\\n\\u308b\\u3067\\'
 b'u3057\\u3087\\u3046\\u300229\\u65e5\\u306f\\u6982\\u306d\\u6674\\u308c\\u3'
 b'06e\\u898b\\u8fbc\\u307f\\u3067\\u3059\\u3002\\n \\u5944\\u7f8e\\u5730\\u65'
 b'b9\\u3067\\u306f\\u300128\\u65e5\\u306f\\u66c7\\u308a\\u6642\\u3005\\u6674'
 b'\\u308c\\u3067\\u3057\\u3087\\u3046\\u300229\\u65e5\\u306f\\u6982\\u306d\\u'
 b'66c7\\u308a\\u306e\\u898b\\u8fbc\\n\\u307f\\u3067\\u3059\\u3002\\n\\n \\u6d7'
 b'7\\u4e0a\\u3067\\u306f\\u300128\\u65e5\\u306f\\u6b21\\u7b2c\\u306b\\u6ce2\\'
 b'u304c\\u9ad8\\u304f\\u306a\\u308b\\u6240\\u304c\\u3042\\u308b\\u3067\\u305'
 b'7\\u3087\\u3046\\u300229\\u65e5\\u306f\\u306f\\u3058\\n\\u3081\\u6ce2\\u304'
 b'c\\u9ad8\\u3044\\u6240\\u304c\\u3042\\u308b\\u898b\\u8fbc\\u307f\\u3067\\u3'
 b'059\\u3002\\n\\n \\u685c\\u5cf6\\u4e0a\\u7a7a\\u304a\\u3088\\u305d1500\\u30'
 b'e1\\u30fc\\u30c8\\u30eb\\u306e\\u98a8\\n 28\\u65e503\\u6642    \\u5357\\u8'
 b'97f\\u306e\\u98a810\\u30e1\\u30fc\\u30c8\\u30eb\\n 28\\u65e512\\u6642\\u30'
 b'6e\\u4e88\\u60f3 \\u897f\\u306e\\u98a813\\u30e1\\u30fc\\u30c8\\u30eb\\n\\n\\'
 b'u003c\\u5929\\u6c17\\u5909\\u5316\\u7b49\\u306e\\u7559\\u610f\\u70b9\\u003'
 b'e\\n \\u5c4b\\u4e45\\u5cf6\\u753a\\u3067\\u306f\\u300128\\u65e5\\u306f\\u66'
 b'c7\\u308a\\u3067\\u3057\\u3087\\u3046\\u300229\\u65e5\\u306f\\u6982\\u306d'
 b'\\u6674\\u308c\\u306e\\u898b\\u8fbc\\u307f\\u3067\\u3059\\u3002\\n \\u5c4b\\'
 b'u4e45\\u5cf6\\u753a\\u3067\\u306f\\u300129\\u65e5\\u307e\\u3067\\u7a7a\\u6'
 b'c17\\u306e\\u4e7e\\u71e5\\u306b\\u3088\\u308b\\u706b\\u306e\\u53d6\\u308a\\'
 b'u6271\\u3044\\u306b\\u6ce8\\u610f\\u3057\\u3066\\u304f\\u3060\\n\\u3055\\u3'
 b'044\\u3002","publicTime":"2019-01-28T04:52:00\\u002b0900"}}').decode('utf-8')

        response_body = WeatherLivedoor.get_city_weather(city_code=CITY_CODE_KAGOSHIMA)

        print(response_body)

        self.assertEqual(kagoshima_weather_forecast, response_body)

