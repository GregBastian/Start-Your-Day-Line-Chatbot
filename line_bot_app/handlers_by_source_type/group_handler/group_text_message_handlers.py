"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.responses.text_message_responses.text_message_responses import \
    text_responses_obj
from line_bot_app.responses.image_message_response.image_message_responses import \
    image_response_obj

from line_bot_app.constants import AcceptedGroupTextMessages


class GroupTextMessageHandlers:
    def group_text_message_handler_function(self, event, line_bot_api, message=""):

        if message == AcceptedGroupTextMessages.CAT.value:
            # returns IMAGE message
            image_response_obj.message_equals_cat(event, line_bot_api)

        elif message == AcceptedGroupTextMessages.DOG.value:
            # returns IMAGE message
            image_response_obj.message_equals_dog(event, line_bot_api)
        
        elif message == AcceptedGroupTextMessages.HELP.value:
            # returns TEXT message
            text_responses_obj.message_equals_help(event, line_bot_api)


group_text_message_event_handlers_obj = GroupTextMessageHandlers()
