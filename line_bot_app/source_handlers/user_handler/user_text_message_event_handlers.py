"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.source_handlers.user_handler.user_text_message_responses import user_text_response
from line_bot_app.source_handlers.user_handler.user_flex_message_responses import user_flex_response


def user_message_event_handler_function(event, line_bot_api, message=""):
    if message == "admin":
        # return TEXT message
        user_text_response.message_equals_admin(event, line_bot_api)

    elif message == "qotd":
        # returns FLEX message
        user_flex_response.message_equals_qotd(event, line_bot_api)
        
    elif message == "p":
        # returns TEXT message
        user_text_response.message_equals_qr(event, line_bot_api)

    elif message == "subscribe":
        pass

    else:
        user_text_response.message_equals_default(event, line_bot_api)

