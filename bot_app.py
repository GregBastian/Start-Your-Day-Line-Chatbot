from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError
from linebot.models import *

bot_app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('uOcExz3z51aHRXtlnHaaKEgLTHj2fN0XNUAoknZDIfz51K5zJLGVdCie9UoBjtam2iv'
                          '+QryLNLxc0Stau7NyvPbvEWjtvh6gsnBUlskp6KZry9yBSJ9ztXFpn0IMm0Rpks2cyl2K9l6+WNVmcbTdTAdB04t89'
                          '/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7266c1cbbd21ef10ef247a977d4cdedd')


if __name__ == '__main__':
    bot_app.run()

