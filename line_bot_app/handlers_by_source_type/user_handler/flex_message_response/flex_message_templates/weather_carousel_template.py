"""
Created on 15/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""


def get_weather_carousel_message(imageUrl="", quoteText="", quoteAuthor=""):
    return {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
            },
            {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Now",
                            "weight": "bold",
                            "align": "center",
                            "color": "#2b2a27"
                        }
                    ],
                    "backgroundColor": "#ffd42b"
                },
                "hero": {
                    "type": "image",
                    "url": "https://openweathermap.org/img/wn/02d@2x.png"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Temp: 25°C",
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
                            "text": "Real Feel: 22°C",
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
                            "text": "heavy intensity rain",
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
        ]
    }
