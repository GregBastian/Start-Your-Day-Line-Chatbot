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

    from line_bot_app.source_handlers import user_handler

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

    @handler.add(MessageEvent, message=TextMessage)
    def text_handler_general(event):
        app.logger.info(f"Received text '{event.message.type}")
        message = event.message.text
        if isinstance(event.source, SourceUser):
            user_handler.user_message_event_handler(event, line_bot_api)

        # if message == "greg":
        #     line_bot_api.reply_message(
        #         event.reply_token,
        #         TextSendMessage("Well, Hello master Greg! What seems to be the problem?")
        #     )
        #
        # elif message == "qr":
        #     line_bot_api.reply_message(
        #         event.reply_token,
        #         TextSendMessage(text='Hello, world',
        #                         quick_reply=QuickReply(items=[
        #                             QuickReplyButton(image_url=QUICK_REPLY_ICONS.get("weather_icon"),
        #                                              action=MessageAction(label="Today's Weather", text="weather")),
        #                             QuickReplyButton(image_url="")
        #                         ]))
        #     )
        # else:
        #     line_bot_api.reply_message(
        #         event.reply_token,
        #         TextSendMessage(message)
        #     )

    return app
