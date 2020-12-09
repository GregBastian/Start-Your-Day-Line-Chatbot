"""
Created on 09/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import *

from line_bot_app.constants import QuickReplyIcons, ADMIN_ID


def message_equals_admin(event, line_bot_api):
    idSender = event.source.user_id
    profile = line_bot_api.get_profile(idSender)
    if idSender == ADMIN_ID:
        emoji = {"index": 0, "productId": "5ac1bfd5040ab15980c9b435", "emojiId": "001"}
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="$foo", emojis=[emoji])
        )
    else:
        profile = line_bot_api.get_profile(idSender)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(f"Tolong {profile.display_name}! Jangan berpura-pura jadi admin")
        )


def message_equals_qr(event, line_bot_api):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="abracadabra",
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(image_url=QuickReplyIcons.WEATHER.value,
                                             action=MessageAction(label="Today's Weather", text="weather")),
                            QuickReplyButton(image_url=QuickReplyIcons.QOTD.value,
                                             action=MessageAction(label="QOTD", text="qotd"))
                        ]))
    )


def message_equals_default(event, line_bot_api):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage("not sure what you're saying there :|")
    )
