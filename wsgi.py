"""
Created on 07/12/2020

@author: Gregorius Ivan Sebastian
@email: ivansebastian60@gmail.com
"""
import os

from linebot import LineBotApi, WebhookHandler

from line_bot_app import create_app

# Channel Access Token
# Get Environment variable for channel secret token stored in CHANNEL ACCESS TOKEN
line_bot_api = LineBotApi("uOcExz3z51aHRXtlnHaaKEgLTHj2fN0XNUAoknZDIfz51K5zJLGVdCie9UoBjtam2iv+QryLNLxc0Stau7NyvPbvEWjtvh6gsnBUlskp6KZry9yBSJ9ztXFpn0IMm0Rpks2cyl2K9l6+WNVmcbTdTAdB04t89/1O/w1cDnyilFU=")

# Channel Secret
# Get Environment variable for channel secret token stored in CHANNEL SECRET
handler = WebhookHandler("7266c1cbbd21ef10ef247a977d4cdedd")


app = create_app(line_bot_api, handler)

if __name__ == "__main__":
    app.run()
