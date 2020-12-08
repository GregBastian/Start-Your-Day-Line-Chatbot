from flask import Flask, request, abort
import logging
import os

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
def hello_greg(event):
    SourceUser
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
                                QuickReplyButton(image_url="https://img.icons8.com/color/48/000000/partly-cloudy-day--v1.png",
                                                 action=MessageAction(label="label", text="text"))
                            ]))
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(message)
        )
