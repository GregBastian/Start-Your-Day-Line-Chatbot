# some future comment

def get_qotd_flex_message(imageUrl="", quoteText="", quoteAuthor=""):
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
                        "label": "Kirim Quote Lagi",
                        "text": "qotd"
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
