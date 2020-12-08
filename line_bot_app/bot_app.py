from flask import Flask, request, abort
import logging
import os
from line_bot_app.image_urls import QUICK_REPLY_ICONS

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# Channel Access Token
# Get Environment variable for channel secret token stored in CHANNEL ACCESS TOKEN
line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])

# Channel Secret
# Get Environment variable for channel secret token stored in CHANNEL SECRET
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route("/")
def homepage():
    return {
        "response": "Hello World",
        "type": "json"
    }


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
    recipientType = event.source.type
    message = event.message.text
    if message == "greg":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("Well, Hello master Greg! What seems to be the problem?")
        )

    elif message == "qr":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Hello, world',
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(image_url=QUICK_REPLY_ICONS.get("weather_icon"),
                                                 action=MessageAction(label="Today's Weather", text="weather")),
                                QuickReplyButton(image_url="")
                            ]))
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(message)
        )
