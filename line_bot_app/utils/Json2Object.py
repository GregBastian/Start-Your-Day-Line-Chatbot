"""
Created on 09/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""
import json
from types import SimpleNamespace


def json2object(jsonObject=None):
    objectResult = json.loads(jsonObject, object_hook=lambda d: SimpleNamespace(**d))
    return objectResult


def json2Object4Qotd(jsonObject=None):
    if jsonObject is None:
        jsonObject = {}
    
    qotdObject = json2object(jsonObject)
    return {
        "qotd": qotdObject.contents.quotes[0].quote,
        "author": qotdObject.contents.quotes[0].author,
        "background": "lol"
    }
