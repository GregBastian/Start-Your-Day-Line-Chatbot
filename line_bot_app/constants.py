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

HELP_FORMAT = ("help", "!help")


class ExtendedEnum(Enum):
    @classmethod
    def names2list(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def values2list(cls):
        return list(map(lambda c: c.value, cls))


class ExternalUrls(ExtendedEnum):
    TROLL_YT_VIDEO = "https://www.youtube.com/watch?v=cqF6M25kqq4"
    RANDOM_DOG_GENERATOR = "https://random.dog/woof.json"
    RANDOM_CAT_GENERATOR = "https://aws.random.cat/meow"


class YoutubeTrollUrls(ExtendedEnum):
    URL_0 = "https://www.youtube.com/watch?v=cqF6M25kqq4"
    URL_1 = "https://www.youtube.com/watch?v=EE-xtCF3T94"
    URL_2 = "https://www.youtube.com/watch?v=j5a0jTc9S10"
    URL_3 = "https://www.youtube.com/watch?v=6-HUgzYPm9g"
    URL_4 = "https://www.youtube.com/watch?v=8O_ifyIIrN4"
    URL_5 = "https://www.youtube.com/watch?v=nHRbZW097Uk"
    URL_6 = "https://www.youtube.com/watch?v=fMnIpIMuBJI"
    URL_7 = "https://www.youtube.com/watch?v=GjyUk_Ebb4o"
    URL_8 = "https://www.youtube.com/watch?v=3KANI2dpXLw"


class ExternalUrlApis(ExtendedEnum):
    QOTD_QUOTES_URL = "https://type.fit/api/quotes"
    QOTD_IMG_URL = "https://picsum.photos/500/350"
    OPENWEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&appid={}&exclude=current," \
                          "minutely,daily,alert&units=metric"
    OPENWEATHER_ICON_URL = "https://openweathermap.org/img/wn/{}@2x.png"


class QuickReplyIcons(ExtendedEnum):
    WEATHER_ICON = "https://img.icons8.com/color/48/000000/partly-cloudy-day--v1.png"
    PIN_ICON = "https://img.icons8.com/color/48/000000/map-pin.png"
    CANCEL_ICON = "https://img.icons8.com/color/48/000000/cancel--v1.png"
    QOTD_ICON = "https://img.icons8.com/flat_round/64/000000/quote.png"


class AcceptedUserTextMessages(ExtendedEnum):
    ADMIN = "admin"
    SUDO_SU = "sudo su"
    QUOTE = "quote"
    WEATHER = "weather"
    TROLL_ME = "troll me"
    CAT = "cat"
    DOG = "dog"
    HELP = "help"


class AcceptedGroupTextMessages(ExtendedEnum):
    ADMIN = "!admin"
    SUDO_SU = "!sudo su"
    CAT = "!cat"
    DOG = "!dog"
    HELP = "!help"
    LEAVE = "!leave"


class AcceptedRoomTextMessages(ExtendedEnum):
    ADMIN = "admin"
    SUDO_SU = "sudo su"
    CAT = "cat"
    DOG = "dog"
    HELP = "help"
    LEAVE = "!leave"


ADMIN_ID = os.getenv("ADMIN_ID", "")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
