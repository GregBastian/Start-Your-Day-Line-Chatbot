# some future comment

def get_qotd_flex_message(imageUrl="", quoteText="", quoteAuthor=""):
    return {
        "type": "bubble",
        "size": "kilo",
        "header": {
            "type": "box",
            "layout": "baseline",
            "contents": [
                {
                    "type": "text",
                    "text": "#Quote of the Day",
                    "weight": "bold",
                    "margin": "none",
                    "size": "xl",
                    "style": "italic",
                    "position": "relative",
                    "align": "center",
                    "decoration": "underline",
                    "color": "#2b2a27"
                }
            ],
            "backgroundColor": "#ffd42b"
        },
        "hero": {
            "type": "image",
            "url": imageUrl,
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
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
                    "align": "start",
                    "adjustMode": "shrink-to-fit",
                    "color": "#2b2a27"
                },
                {
                    "type": "text",
                    "text": quoteAuthor,
                    "margin": "sm",
                    "size": "sm",
                    "color": "#2b2a2a"
                }
            ],
            "backgroundColor": "#ffd42b"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "message",
                        "label": "Get Another Quote",
                        "text": "qotd"
                    }
                },
                {
                    "type": "spacer",
                    "size": "sm"
                }
            ],
            "flex": 0
        }
    }
