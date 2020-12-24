"""
Created on 09/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import *

from line_bot_app.constants import ExternalUrls

import requests


class UserImageResponse:
    def message_startswith_random_and_endswith_cat(self, event, line_bot_api):
        while True:
            media = requests.get(ExternalUrls.RANDOM_CAT_GENERATOR.value).json()['file']
            if media.lower().endswith(('.png', '.jpg', '.jpeg')):
                line_bot_api.reply_message(
                    event.reply_token,
                    ImageSendMessage(media, media)
                )
                break

    def message_startswith_random_and_endswith_dog(self, event, line_bot_api):
        while True:
            media = requests.get(ExternalUrls.RANDOM_DOG_GENERATOR.value).json()['url']
            if media.lower().endswith(('.png', '.jpg', '.jpeg')):
                line_bot_api.reply_message(
                    event.reply_token,
                    ImageSendMessage(media, media)
                )
                break


user_image_response_obj = UserImageResponse()
