# some future comment

from line_bot_app.constants import AcceptedGroupTextMessages

import random


def get_quote_flex_message(quotesAndAuthors="", imageUrl="", quoteText="", quoteAuthor=""):
    randomEntryInResponse = random.choice(quotesAndAuthors)
    quoteText, quoteAuthor = randomEntryInResponse.get("text", ""), randomEntryInResponse.get("author", "")
    return {
        "type": "bubble",
        "size": "kilo",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "#Random Quote",
                    "weight": "bold",
                    "style": "italic",
                    "decoration": "underline",
                    "align": "center",
                    "size": "xl",
                    "margin": "xs",
                    "color": "#2b2a27"
                }
            ],
            "backgroundColor": "#ffd42b"
        },
        "hero": {
            "type": "image",
            "url": imageUrl,
            "size": "full",
            "aspectRatio": "17:10",
            "aspectMode": "cover",
            "margin": "none"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": quoteText,
                    "weight": "bold",
                    "size": "lg",
                    "wrap": True,
                    "color": "#2b2a27"
                },
                {
                    "type": "text",
                    "text": "~" + quoteAuthor + "~",
                    "margin": "sm",
                    "color": "#2b2a2a"
                }
            ],
            "backgroundColor": "#ffd42b",
            "borderWidth": "none",
            "cornerRadius": "none",
            "margin": "none",
            "spacing": "none"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "message",
                        "label": "Another Quote Please",
                        "text": AcceptedGroupTextMessages.QUOTE.value
                    },
                    "position": "relative",
                    "margin": "sm",
                    "height": "sm",
                    "style": "primary",
                    "color": "#e6be20"
                }
            ],
            "flex": 0
        }
    }
