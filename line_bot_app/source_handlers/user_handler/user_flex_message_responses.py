"""
Created on 11/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

import random
import requests
from linebot.models import FlexSendMessage, BubbleContainer, BoxComponent, TextComponent, ImageComponent

from line_bot_app.constants import ExternalUrlApis

from line_bot_app.source_handlers.user_handler.flex_message_templates.qotd_flex_template import get_qotd_flex_message


class UserFlexResponse:

    def message_equals_qotd(self, event, line_bot_api):
        image = requests.get(ExternalUrlApis.QOTD_IMG_URL.value)
        quotesAndAuthors = (requests.get(ExternalUrlApis.QOTD_QUOTES_URL.value)).json()
        randomEntryInResponse = random.choice(quotesAndAuthors)
        quote, author = randomEntryInResponse.get("text", ""), randomEntryInResponse.get("author", "")
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(get_qotd_flex_message(image, quote, author))
        )


user_flex_response = UserFlexResponse()
