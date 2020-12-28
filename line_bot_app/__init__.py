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

from line_bot_app.handlers_by_source_type.user_handler.location_message_handlers import \
    location_message_event_handlers_obj

from line_bot_app.handlers_by_source_type.user_handler.user_text_message_handlers import \
    user_text_message_event_handlers_obj

from line_bot_app.utils.help_message_util import help_message_obj


def create_app(line_bot_api, handler):
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)

    @app.route("/test")
    def homepage_test():
        return {
            "message": "Hello World",
            "type": "json"
        }

    @app.route("/webhook", methods=['POST'])
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

    @handler.add(FollowEvent)
    def user_follow_event(event):
        idUser = event.source.user_id
        profile = line_bot_api.get_profile(idUser)
        app.logger.info(f"Received Follow event from {idUser}")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(help_message_obj.help_message_user(profile.display_name))
        )

    @handler.add(JoinEvent)
    def join_handler(event):
        if isinstance(event.source, SourceRoom):
            app.logger.info(f"Received JoinEvent {event.message.text} from SourceRoom with id '{event.source.user_id}'")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(help_message_obj.help_message_group(event.source.group_id))
            )

        elif isinstance(event.source, SourceGroup):
            app.logger.info(
                f"Received TextMessage {event.message.text} from SourceGroup with id '{event.source.user_id}'")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(help_message_obj.help_message_group(event.source.room_id))
            )

    @handler.add(MessageEvent, message=TextMessage)
    def text_handler_general(event):
        message = str(event.message.text).lower()
        if isinstance(event.source, SourceUser):
            app.logger.info(
                f"Received TextMessage {event.message.text} from SourceUser with id '{event.source.user_id}'")
            user_text_message_event_handlers_obj.user_text_message_handler_function(event, line_bot_api, message)

        elif isinstance(event.source, SourceGroup):
            app.logger.info(
                f"Received TextMessage {event.message.text} from SourceGroup with id '{event.source.user_id}'")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage("Feature is not implemented yet")
            )

        elif isinstance(event.source, SourceRoom):
            app.logger.info(
                f"Received TextMessage {event.message.text} from SourceRoom with id '{event.source.user_id}'")
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage("Feature is not implemented yet")
            )

    @handler.add(MessageEvent, message=LocationMessage)
    def location_handler_general(event):
        if isinstance(event.source, SourceUser):
            app.logger.info(f"Received LocationMessage from {event.source} with id '{event.source.user_id}'")
            location_message_event_handlers_obj.user_location_message_handler_function(event, line_bot_api)
        else:
            app.logger.info(f"Received LocationMessage from {event.source} with id '{event.source.user_id}'. "
                            f"App will not reply because LocationMessages from {event.source} will not be handled'")

    @handler.default()
    def default(event):
        app.logger.info(f"Received Unhandled event {event} from {event.source} with id '{event.source.user_id}'")

    return app
