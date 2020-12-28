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
    timezoneOffset = weatherDataHourly["timezone_offset"]
    for index, data in enumerate(weatherDataHourly["hourly"][:20:2]):
        if index == 0:
            time = "Now"
        else:
            time = datetime.utcfromtimestamp(data["dt"]+timezoneOffset).strftime('%H:%M')
        temp = str(round(data["temp"])) + "°C"
        realFeelTemp = str(round(data["feels_like"])) + "°C"
        weatherDesc = data["weather"][0]["description"]
        weatherIcon = data["weather"][0]["icon"]
        bubbleContents.append(get_weather_bubble_message(time, weatherIcon, temp, realFeelTemp, weatherDesc))

    return {
        "type": "carousel",
        "contents": bubbleContents
    }

    # {
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
    #                         "text": "Temp: 25°C",
    #                         "color": "#2b2a27",
    #                         "align": "center",
    #                         "margin": "md",
    #                         "size": "lg"
    #                     },
    #                     {
    #                         "type": "separator",
    #                         "color": "#2b2a27",
    #                         "margin": "none"
    #                     },
    #                     {
    #                         "type": "text",
    #                         "text": "Real Feel: 22°C",
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
    #                         "wrap": true
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
