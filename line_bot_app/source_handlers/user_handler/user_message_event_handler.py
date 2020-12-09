"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from line_bot_app.source_handlers.user_handler.response_by_message import *


def user_message_event_handler_function(event, line_bot_api, message=""):
    if message == "admin":
        message_equals_admin(event, line_bot_api)

    elif message == "qr":
        message_equals_qr(event, line_bot_api)

    else:
        message_equals_default(event, line_bot_api)

