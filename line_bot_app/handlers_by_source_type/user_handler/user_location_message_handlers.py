"""
Created on 13/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.handlers_by_source_type.user_handler.flex_message_response.user_flex_message_responses import \
    user_flex_response_obj


class UserLocationMessageHandlers:
    def user_location_message_handler_function(self, event, line_bot_api):
        user_flex_response_obj.location_equals_received_location(event, line_bot_api)


user_location_message_event_handlers_obj = UserLocationMessageHandlers()
