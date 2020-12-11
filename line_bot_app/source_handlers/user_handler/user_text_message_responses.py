"""
Created on 09/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import *

from line_bot_app.constants import QuickReplyIcons, ADMIN_ID


class UserTextResponse:
    def message_equals_admin(self, event, line_bot_api):
        idSender = event.source.user_id
        profile = line_bot_api.get_profile(idSender)
        if idSender == ADMIN_ID:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"Halo Tuan {profile.display_name}! Ada yang bisa saya bantu?")
            )
        else:
            profile = line_bot_api.get_profile(idSender)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"Tolong {profile.display_name}! Jangan berpura-pura jadi admin")
            )

    def message_equals_qr(self, event, line_bot_api):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="abracadabra",
                            quick_reply=QuickReply(items=[
                                # QuickReplyButton(image_url=QuickReplyIcons.WEATHER.value,
                                #                  action=MessageAction(label="Today's Weather", text="weather")),
                                QuickReplyButton(image_url=QuickReplyIcons.QOTD.value,
                                                 action=MessageAction(label="QOTD", text="qotd"))
                            ]))
        )

    def message_equals_devnews(self, event, line_bot_api):
        pass


    def message_equals_default(self, event, line_bot_api):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("not sure what you're saying there :|")
        )


user_text_response = UserTextResponse()