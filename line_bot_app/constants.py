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


class ExternalUrlApis(Enum):
    QOTD_QUOTES_URL = "https://type.fit/api/quotes"
    QOTD_IMG_URL = "https://picsum.photos/500/350"


class QuickReplyIcons(Enum):
    WEATHER_ICON = "https://img.icons8.com/color/48/000000/partly-cloudy-day--v1.png"
    QOTD_ICON = "https://img.icons8.com/flat_round/64/000000/quote.png"


ADMIN_ID = os.getenv("ADMIN_ID", "")
