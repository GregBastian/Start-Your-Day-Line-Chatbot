from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('uOcExz3z51aHRXtlnHaaKEgLTHj2fN0XNUAoknZDIfz51K5zJLGVdCie9UoBjtam2iv'
                          '+QryLNLxc0Stau7NyvPbvEWjtvh6gsnBUlskp6KZry9yBSJ9ztXFpn0IMm0Rpks2cyl2K9l6+WNVmcbTdTAdB04t89'
                          '/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7266c1cbbd21ef10ef247a977d4cdedd')


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
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(message)
        )


@handler.add(MessageEvent, message=TextMessage)
def hello_ines(event):
    SourceUser
    message = event.message.text
    if message == "greg":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("Well, Hello master Greg! What seems to be the problem?")
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(message)
        )
