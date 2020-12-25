"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.responses.text_message_responses.user_text_message_responses import \
    image_responses_obj
from line_bot_app.responses.flex_message_response.flex_message_responses import \
    flex_responses_obj
from line_bot_app.responses.image_message_response.image_message_responses import \
    user_image_response_obj

from line_bot_app.constants import AcceptedTextMessages


class UserTextMessageHandlers:
    def user_text_message_handler_function(self, event, line_bot_api, message=""):
        if message == AcceptedTextMessages.ADMIN.value or message == AcceptedTextMessages.SUDO_SU.value:
            # return TEXT message
            image_responses_obj.message_equals_admin(event, line_bot_api)

        elif message == AcceptedTextMessages.QUOTE.value:
            # returns FLEX message
            flex_responses_obj.message_equals_quote(event, line_bot_api)

        elif message == AcceptedTextMessages.WEATHER.value:
            # returns TEXT message and QUICK REPLY
            image_responses_obj.message_equals_weather(event, line_bot_api)

        elif message == AcceptedTextMessages.TROLL_ME.value:
            # return TEXT message
            image_responses_obj.message_equals_troll_me(event, line_bot_api)

        elif message in [AcceptedTextMessages.CAT.value, AcceptedTextMessages.DOG.value]:
            if message == AcceptedTextMessages.CAT.value:
                user_image_response_obj.message_equals_cat(event, line_bot_api)
            elif message == AcceptedTextMessages.DOG.value:
                user_image_response_obj.message_equals_dog(event, line_bot_api)
        
        elif message == AcceptedTextMessages.HELP.value:
            image_responses_obj.message_equals_help(event, line_bot_api)

        else:
            image_responses_obj.message_equals_default(event, line_bot_api)


user_text_message_event_handlers_obj = UserTextMessageHandlers()
