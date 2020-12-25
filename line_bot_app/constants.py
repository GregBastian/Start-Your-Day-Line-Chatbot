"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
import os
from enum import Enum

QUICK_REPLY_ICONS = {
    "weather_icon": "https://img.icons8.com/color/48/000000/partly-cloudy-day--v1.png"
}


class ExternalUrls(Enum):
    TROLL_YT_VIDEO = "https://www.youtube.com/watch?v=cqF6M25kqq4"
    RANDOM_DOG_GENERATOR = "https://random.dog/woof.json"
    RANDOM_CAT_GENERATOR = "https://aws.random.cat/meow"


class ExternalUrlApis(Enum):
    QOTD_QUOTES_URL = "https://type.fit/api/quotes"
    QOTD_IMG_URL = "https://picsum.photos/500/350"
    OPENWEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&exclude=current," \
                          "minutely,daily,alert&units=metric"
    OPENWEATHER_ICON_URL = "https://openweathermap.org/img/wn/{}@2x.png"


class QuickReplyIcons(Enum):
    WEATHER_ICON = "https://img.icons8.com/color/48/000000/partly-cloudy-day--v1.png"
    PIN_ICON = "https://img.icons8.com/color/48/000000/map-pin.png"
    CANCEL_ICON = "https://img.icons8.com/color/48/000000/cancel--v1.png"
    QOTD_ICON = "https://img.icons8.com/flat_round/64/000000/quote.png"


class AcceptedTextMessages(Enum):
    ADMIN = "admin"
    SUDO_SU = "sudo su"
    QUOTE = "quote"
    WEATHER = "weather"
    TROLL_ME = "troll me"
    CAT = "cat"
    DOG = "dog"
    HELP = "help"

    @staticmethod
    def names2list():
        return list(map(lambda c: c.name, AcceptedTextMessages))

    @staticmethod
    def values2list():
        return list(map(lambda c: c.value, AcceptedTextMessages))


ADMIN_ID = os.getenv("ADMIN_ID", "")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
