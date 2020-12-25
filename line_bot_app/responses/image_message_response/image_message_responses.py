"""
Created on 09/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import *

from line_bot_app.constants import ExternalUrls

import requests


class ImageResponse:
    def message_equals_cat(self, event, line_bot_api):
        while True:
            # put into loop because sometimes the requested media can be a video
            media = requests.get(ExternalUrls.RANDOM_CAT_GENERATOR.value).json()['file']
            if media.lower().endswith(('.png', '.jpg', '.jpeg')):
                line_bot_api.reply_message(
                    event.reply_token,
                    ImageSendMessage(media, media)
                )
                break

    def message_equals_dog(self, event, line_bot_api):
        while True:
            # put into loop because sometimes the requested media can be a video
            media = requests.get(ExternalUrls.RANDOM_DOG_GENERATOR.value).json()['url']
            if media.lower().endswith(('.png', '.jpg', '.jpeg')):
                line_bot_api.reply_message(
                    event.reply_token,
                    ImageSendMessage(media, media)
                )
                break


image_response_obj = ImageResponse()
