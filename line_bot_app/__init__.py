"""
Created on 08/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
from flask import Flask, request, abort
import logging

from linebot.exceptions import InvalidSignatureError
from linebot.models import *


def create_app(line_bot_api, handler):
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route("/callback", methods=['POST'])
    def callback():
        # get X-Line-Signature header value
        signature = request.headers['X-Line-Signature']
        # get request body as text
        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)
        # handle webhook body
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)
        return 'OK'

    from line_bot_app.handlers_by_source_type.user_handler.user_text_message_handlers import \
        user_text_message_event_handlers_obj

    @handler.add(MessageEvent, message=TextMessage)
    def text_handler_general(event):
        message = str(event.message.text).lower()
        if isinstance(event.source, SourceUser):
            app.logger.info(f"Received TextMessage from SourceUser with id '{event.source.user_id}'")
            user_text_message_event_handlers_obj.user_text_message_handler_function(event, line_bot_api, message)

        elif isinstance(event.source, SourceGroup):
            app.logger.info(f"Received TextMessage from SourceGroup with id '{event.source.user_id}'")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage("Feature is not implemented yet")
            )
        elif isinstance(event.source, SourceRoom):
            app.logger.info(f"Received TextMessage from SourceRoom with id '{event.source.user_id}'")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage("Feature is not implemented yet")
            )

    from line_bot_app.handlers_by_source_type.user_handler.user_location_message_handlers import \
        user_location_message_event_handlers_obj

    @handler.add(MessageEvent, message=LocationMessage)
    def location_handler_general(event):
        if isinstance(event.source, SourceUser):
            app.logger.info(f"Received LocationMessage from {event.source} with id '{event.source.user_id}'")
            user_location_message_event_handlers_obj.user_location_message_handler_function(event, line_bot_api)
        else:
            app.logger.info(f"Received LocationMessage from {event.source} with id '{event.source.user_id}'")
            app.logger.info(f"Will not reply because LocationMessages from {event.source} will not be handled'")
            pass

    return app
