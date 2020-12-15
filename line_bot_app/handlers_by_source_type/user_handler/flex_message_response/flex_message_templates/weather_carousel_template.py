"""
Created on 15/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from datetime import datetime


def get_weather_bubble_message(displayTime="", weatherIconCode="", temp="", realFeelTemp="", weatherDescription=""):
    return {
        "type": "bubble",
        "size": "micro",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": displayTime,
                    "weight": "bold",
                    "align": "center",
                    "color": "#2b2a27"
                }
            ],
            "backgroundColor": "#ffd42b"
        },
        "hero": {
            "type": "image",
            "url": f"https://openweathermap.org/img/wn/{weatherIconCode}@2x.png"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": f"Temp: {temp}",
                    "color": "#2b2a27",
                    "align": "center",
                    "margin": "md"
                },
                {
                    "type": "separator",
                    "color": "#2b2a27",
                    "margin": "none"
                },
                {
                    "type": "text",
                    "text": f"Real Feel: {realFeelTemp}",
                    "margin": "md",
                    "align": "center",
                    "color": "#2b2a27"
                },
                {
                    "type": "separator",
                    "color": "#2b2a27",
                    "margin": "sm"
                },
                {
                    "type": "text",
                    "text": weatherDescription,
                    "align": "center",
                    "color": "#2b2a27",
                    "margin": "md",
                    "wrap": True
                }
            ],
            "backgroundColor": "#ffd42b",
            "margin": "none"
        },
        "styles": {
            "hero": {
                "backgroundColor": "#9bb1fa"
            }
        }
    }


def get_weather_carousel_message(weatherDataHourly={}):
    bubbleContents = []
    for data in weatherDataHourly["hourly"][:20:2]:
        timezoneOffset = data["timezone_offset"]
        time = datetime.utcfromtimestamp(data["dt"]+timezoneOffset).strftime('%H:%M')
        temp = data["temp"]
        realFeelTemp = data["feels_like"]
        weatherDesc, weatherIcon = data["weather"][0]["description"], data["weather"][0]["icon"]
        bubbleContents.append(get_weather_bubble_message(time, weatherIcon, temp, realFeelTemp, weatherDesc))

    return {
        "type": "carousel",
        "contents": bubbleContents
    }

    # return {
    #     "type": "carousel",
    #     "contents": [
    #         {
    #             "type": "bubble",
    #             "size": "micro",
    #             "header": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Now",
    #                         "weight": "bold",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b"
    #             },
    #             "hero": {
    #                 "type": "image",
    #                 "url": "https://openweathermap.org/img/wn/02d@2x.png"
    #             },
    #             "body": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Temp: 25C",
    #                         "color": "#2b2a27",
    #                         "align": "center",
    #                         "margin": "md"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "none"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "Real Feel: 22C",
    #                         "margin": "md",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "sm"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "heavy intensity rain",
    #                         "align": "center",
    #                         "color": "#2b2a27",
    #                         "margin": "md",
    #                         "wrap": True
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b",
    #                 "margin": "none"
    #             },
    #             "styles": {
    #                 "hero": {
    #                     "backgroundColor": "#9bb1fa"
    #                 }
    #             }
    #         },
    #         {
    #             "type": "bubble",
    #             "size": "micro",
    #             "header": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Now",
    #                         "weight": "bold",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b"
    #             },
    #             "hero": {
    #                 "type": "image",
    #                 "url": "https://openweathermap.org/img/wn/02d@2x.png"
    #             },
    #             "body": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Temp: 25C",
    #                         "color": "#2b2a27",
    #                         "align": "center",
    #                         "margin": "md"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "none"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "Real Feel: 22C",
    #                         "margin": "md",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "sm"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "heavy intensity rain",
    #                         "align": "center",
    #                         "color": "#2b2a27",
    #                         "margin": "md",
    #                         "wrap": True
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b",
    #                 "margin": "none"
    #             },
    #             "styles": {
    #                 "hero": {
    #                     "backgroundColor": "#9bb1fa"
    #                 }
    #             }
    #         },
    #         {
    #             "type": "bubble",
    #             "size": "micro",
    #             "header": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Now",
    #                         "weight": "bold",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b"
    #             },
    #             "hero": {
    #                 "type": "image",
    #                 "url": "https://openweathermap.org/img/wn/02d@2x.png"
    #             },
    #             "body": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Temp: 25C",
    #                         "color": "#2b2a27",
    #                         "align": "center",
    #                         "margin": "md"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "none"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "Real Feel: 22C",
    #                         "margin": "md",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "sm"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "heavy intensity rain",
    #                         "align": "center",
    #                         "color": "#2b2a27",
    #                         "margin": "md",
    #                         "wrap": True
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b",
    #                 "margin": "none"
    #             },
    #             "styles": {
    #                 "hero": {
    #                     "backgroundColor": "#9bb1fa"
    #                 }
    #             }
    #         },
    #         {
    #             "type": "bubble",
    #             "size": "micro",
    #             "header": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Now",
    #                         "weight": "bold",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b"
    #             },
    #             "hero": {
    #                 "type": "image",
    #                 "url": "https://openweathermap.org/img/wn/02d@2x.png"
    #             },
    #             "body": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Temp: 25C",
    #                         "color": "#2b2a27",
    #                         "align": "center",
    #                         "margin": "md"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "none"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "Real Feel: 22C",
    #                         "margin": "md",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "sm"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "heavy intensity rain",
    #                         "align": "center",
    #                         "color": "#2b2a27",
    #                         "margin": "md",
    #                         "wrap": True
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b",
    #                 "margin": "none"
    #             },
    #             "styles": {
    #                 "hero": {
    #                     "backgroundColor": "#9bb1fa"
    #                 }
    #             }
    #         },
    #         {
    #             "type": "bubble",
    #             "size": "micro",
    #             "header": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Now",
    #                         "weight": "bold",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b"
    #             },
    #             "hero": {
    #                 "type": "image",
    #                 "url": "https://openweathermap.org/img/wn/02d@2x.png"
    #             },
    #             "body": {
    #                 "type": "box",
    #                 "layout": "vertical",
    #                 "contents": [
    #                     {
    #                         "type": "text",
    #                         "text": "Temp: 25C",
    #                         "color": "#2b2a27",
    #                         "align": "center",
    #                         "margin": "md"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "none"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "Real Feel: 22C",
    #                         "margin": "md",
    #                         "align": "center",
    #                         "color": "#2b2a27"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "sm"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "heavy intensity rain",
    #                         "align": "center",
    #                         "color": "#2b2a27",
    #                         "margin": "md",
    #                         "wrap": True
    #                     }
    #                 ],
    #                 "backgroundColor": "#ffd42b",
    #                 "margin": "none"
    #             },
    #             "styles": {
    #                 "hero": {
    #                     "backgroundColor": "#9bb1fa"
    #                 }
    #             }
    #         }
    #     ]
    # }
