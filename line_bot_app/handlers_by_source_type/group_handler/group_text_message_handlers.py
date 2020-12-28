"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.responses.text_message_responses.text_message_responses import \
    text_responses_obj
from line_bot_app.responses.flex_message_response.flex_message_responses import \
    flex_responses_obj
from line_bot_app.responses.image_message_response.image_message_responses import \
    image_response_obj

from line_bot_app.constants import AcceptedTextMessages


class GroupTextMessageHandlers:
    def group_text_message_handler_function(self, event, line_bot_api, message=""):

        if message == AcceptedTextMessages.CAT.value:
            # returns IMAGE message
            image_response_obj.message_equals_cat(event, line_bot_api)

        elif message == AcceptedTextMessages.DOG.value:
            # returns TEXT message
            image_response_obj.message_equals_dog(event, line_bot_api)
        
        elif message == AcceptedTextMessages.HELP.value:
            # returns TEXT message
            text_responses_obj.message_equals_help(event, line_bot_api)

        else:
            text_responses_obj.fallback_message(event, line_bot_api)


user_text_message_event_handlers_obj = GroupTextMessageHandlers()
