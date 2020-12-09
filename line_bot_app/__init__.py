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

    from line_bot_app.source_handlers.user_handler import user_message_event_handler

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

    @handler.add(MessageEvent, message=TextMessage)
    def text_handler_general(event):
        message = str(event.message.text).lower()
        if isinstance(event.source, SourceUser):
            app.logger.info(f"Received SourceUser text message in  from id '{event.source.user_id}'")
            user_message_event_handler.user_message_event_handler_function(event, line_bot_api, message)

        elif isinstance(event.source, SourceGroup):
            app.logger.info(f"Received SourceGroup text message in from id '{event.source.user_id}'")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage("Feature is not implemented yet")
            )
        elif isinstance(event.source, SourceRoom):
            app.logger.info(f"Received SourceRoom text message in from id '{event.source.user_id}'")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage("Feature is not implemented yet")
            )

    return app
