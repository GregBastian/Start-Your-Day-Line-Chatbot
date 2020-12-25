"""
Created on 09/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import *

from line_bot_app.constants import QuickReplyIcons, ADMIN_ID, ExternalUrls, AcceptedTextMessages

import difflib


class ImageResponses:
    def message_equals_admin(self, event, line_bot_api):
        idSender = event.source.user_id
        profile = line_bot_api.get_profile(idSender)
        if idSender == ADMIN_ID:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"Halo Tuan {profile.display_name}! Ada yang bisa saya bantu?")
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"Tolong ya {profile.display_name}... Jangan berpura-pura jadi admin")
            )

    def message_equals_weather(self, event, line_bot_api):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Silahkan mengirimkan lokasi dengan menekan tombol dibawah untuk mendapatkan laporan "
                                 "cuaca terkini",
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(image_url=QuickReplyIcons.PIN_ICON.value,
                                                 action=LocationAction(label="Send Location"))
                            ]))
        )

    def message_equals_troll_me(self, event, line_bot_api):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(ExternalUrls.TROLL_YT_VIDEO.value)
        )

    def message_equals_default(self, event, line_bot_api):
        message = event.message.text
        acceptedMessages = AcceptedTextMessages.values2list()
        closestMatch = difflib.get_close_matches(message, acceptedMessages, 1, 0.4)

        if len(closestMatch) == 1:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"Mungkin maksudmu {closestMatch[0]}?\n\n"
                                "Coba ketik 'help' untuk melihat semua perintah yang aku pahami.")
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage("Aku kurang paham maksudmu. Coba ketik 'help' untuk melihat semua perintah "
                                "yang aku pahami.")
            )
            pass


image_responses_obj = ImageResponses()
