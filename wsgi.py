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
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN', None))

# Channel Secret
# Get Environment variable for channel secret token stored in CHANNEL SECRET
handler = WebhookHandler(os.getenv('CHANNEL_SECRET', None))


app = create_app(line_bot_api, handler)

if __name__ == "__main__":
    app.run()
