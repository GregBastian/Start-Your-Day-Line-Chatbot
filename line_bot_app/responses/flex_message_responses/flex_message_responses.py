"""
Created on 11/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

import requests
from datetime import datetime
from linebot.models import FlexSendMessage, TextSendMessage

# for URLS
from line_bot_app.constants import ExternalUrlApis

# for constant singular values like API keys
from line_bot_app.constants import OPENWEATHER_API_KEY

from line_bot_app.responses.flex_message_responses.flex_message_templates.quote_flex_template \
    import get_quote_flex_message

from line_bot_app.responses.flex_message_responses.flex_message_templates.weather_carousel_template \
    import get_weather_carousel_message


class FlexResponses:

    def message_equals_quote(self, event, line_bot_api):
        image = (requests.get(ExternalUrlApis.QOTD_IMG_URL.value)).url
        quotesAndAuthors = requests.get(ExternalUrlApis.QOTD_QUOTES_URL.value).json()

        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(alt_text="Random Quote", contents=get_quote_flex_message(quotesAndAuthors, image))
        )

    def location_equals_received_location(self, event, line_bot_api):
        userLat = event.message.latitude
        userLong = event.message.longitude
        weatherDataHourly = requests.get(
            ExternalUrlApis.OPENWEATHER_API_URL.value.format(userLat, userLong, OPENWEATHER_API_KEY)).json()

        timeNow = weatherDataHourly["timezone_offset"] + weatherDataHourly["hourly"][0]["dt"]
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text=f"Data disediakan oleh OpenWeather (https://openweathermap.org/)\n\n"
                                     f"Waktu Sekarang adalah: "
                                     f"{datetime.utcfromtimestamp(timeNow).strftime('%d-%m-%Y %H:%M')}"),
                FlexSendMessage(alt_text='Weather Report', contents=get_weather_carousel_message(weatherDataHourly)),
            ]
        )


flex_responses_obj = FlexResponses()
