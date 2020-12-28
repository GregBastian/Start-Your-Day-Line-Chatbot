"""
Created on 29/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""

from linebot.models import *


class LeaveResponses:
    def leave_group(self, event, line_bot_api):
        groupInfo = line_bot_api.get_group_summary(event.source.group_id)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(f"Goodbye people {groupInfo.group_name}! I will miss all of you :)"))
        line_bot_api.leave_group(event.source.group_id)


leave_response_obj = LeaveResponses()