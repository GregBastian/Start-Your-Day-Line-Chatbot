"""
Created on 09/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import *

from line_bot_app.constants import QuickReplyIcons, ADMIN_ID, AcceptedTextMessages, YoutubeTrollUrls

from line_bot_app.utils.help_message_util import help_message_obj

import difflib

import random


class TextResponses:
    def message_equals_admin(self, event, line_bot_api):
        idUser = event.source.user_id
        profile = line_bot_api.get_profile(idUser)
        if idUser == ADMIN_ID:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"Hello Master {profile.display_name}! How may I be of service?")
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"hey {profile.display_name}... don't you dare fake as an admin")
            )

    def message_equals_weather(self, event, line_bot_api):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Please send your location by tapping the button below to get "
                                 "your weather report.",
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(image_url=QuickReplyIcons.PIN_ICON.value,
                                                 action=LocationAction(label="Send Location"))
                            ]))
        )

    def message_equals_troll_me(self, event, line_bot_api):
        randomTrollVideoUrl = random.choice(YoutubeTrollUrls.values2list())
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(randomTrollVideoUrl)
        )

    def message_equals_help(self, event, line_bot_api):
        idUser = event.source.user_id
        profile = line_bot_api.get_profile(idUser)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(help_message_obj.help_message_user(profile.display_name))
        )

    def fallback_message(self, event, line_bot_api):
        message = event.message.text
        acceptedMessages = AcceptedTextMessages.values2list()
        closestMatch = difflib.get_close_matches(message, acceptedMessages, 1, 0.4)

        # check if theres anything in the list 'closestMatch'
        if closestMatch:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"Do you mean {closestMatch[0]}?\n\n"
                                "Try typing 'help' too see all the commands which I understand.")
            )
        else:
            if isinstance(event.source, SourceGroup) or isinstance(event.source, SourceRoom):
                helpFormat = "!help"
            else:
                helpFormat = "help"
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"I don't understand what you mean. Try typing '{helpFormat}' too see all the commands"
                                "which I understand.")
            )




text_responses_obj = TextResponses()
