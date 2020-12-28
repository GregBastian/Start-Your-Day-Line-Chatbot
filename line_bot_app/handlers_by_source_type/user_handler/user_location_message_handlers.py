"""
Created on 13/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.responses.flex_message_responses.flex_message_responses import \
    flex_responses_obj


class UserLocationMessageHandlers:
    def user_location_message_handler_function(self, event, line_bot_api):
        flex_responses_obj.location_equals_received_location(event, line_bot_api)


user_location_message_event_handlers_obj = UserLocationMessageHandlers()
