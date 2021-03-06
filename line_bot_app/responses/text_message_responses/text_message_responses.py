"""
Created on 09/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import *

from line_bot_app.constants import QuickReplyIcons, ADMIN_ID, AcceptedUserTextMessages, AcceptedGroupTextMessages, \
    YoutubeTrollUrls, HELP_FORMAT

from line_bot_app.responses.text_message_responses.text_message_templates.help_message_template import help_message_obj

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
                TextSendMessage(f"Hey {profile.display_name}... don't you dare fake as an admin")
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
        if isinstance(event.source, SourceUser):
            userInfo = line_bot_api.get_profile(event.source.user_id)
            helpMessage = TextSendMessage(help_message_obj.help_message_user(userInfo.display_name))
        elif isinstance(event.source, SourceGroup):
            groupInfo = line_bot_api.get_group_summary(event.source.group_id)
            helpMessage = TextSendMessage(help_message_obj.help_message_group(groupInfo.group_name))

        line_bot_api.reply_message(
            event.reply_token,
            helpMessage
        )

    def fallback_message(self, event, line_bot_api):
        message = event.message.text
        closestMatch = difflib.get_close_matches(message, AcceptedUserTextMessages.values2list(), 1, 0.4)

        # check if theres anything in the list 'closestMatch'
        if closestMatch:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"Did you mean '{closestMatch[0]}'?\n\n"
                                f"Try typing '{AcceptedUserTextMessages.HELP.value}' too see all the commands which I "
                                f"understand.")
            )

        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"I don't understand what you mean. Try typing '{AcceptedUserTextMessages.HELP.value}' "
                                f"too see all the commands which I understand.")
            )

    def group_fallback_message(self, event, line_bot_api):
        message = event.message.text
        acceptedMessages = AcceptedGroupTextMessages.values2list()
        closestMatch = difflib.get_close_matches(message, acceptedMessages, 1, 0.4)

        # check if theres anything in the list 'closestMatch'
        if closestMatch:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(f"Did you mean '!{closestMatch[0]}'?\n\n"
                                f"Try typing '{HELP_FORMAT[1]}' too see all the commands which I understand.")
            )


text_responses_obj = TextResponses()
