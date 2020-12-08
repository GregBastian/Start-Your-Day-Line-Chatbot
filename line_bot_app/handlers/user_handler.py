"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from line_bot_app import handler, line_bot_api
from linebot.models import *

from line_bot_app.image_urls import QUICK_REPLY_ICONS


def user_message_event_handler(event):
    message = event.message.text
    if message == "greg":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("Well, Hello master Greg! What seems to be the problem?")
        )

    elif message == "qr":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Hello, world',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(image_url=QUICK_REPLY_ICONS.get("weather_icon"),
                                                 action=MessageAction(label="Today's Weather", text="weather")),
                                QuickReplyButton(image_url="")
                            ]))
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(message)
        )