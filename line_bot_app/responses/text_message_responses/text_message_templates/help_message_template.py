"""
Created on 09/12/2020

@author: Gregorius Ivan Sebastian
@office: Sprint Asia Technology
@email: greg.sebastian@sprintasia.co.id / ivansebastian60@gmail.com
"""


class HelpMessageUtil:
    def help_message_user(self, userDisplayName="USER_NAME"):
        return f"Hello, {userDisplayName}!\n" \
               "Write these commands (or use the menu), so I " \
               "can start your day off properly:\n" \
               "1. 'quote' (Get Random Quote): get a wise quote\n" \
               "2. 'weather' (Get Weather Report): get weather report for the next 18 hours\n" \
               "3. 'troll me' (Troll Me): do i need to explain?\n" \
               "4. 'dog' (Get Dog Pic): start your day with a cute random dog image\n" \
               "5. 'cat' (Get Cat Pic): start your day with an adorable random cat image\n" \
               "6. 'help' (Help): display this message again"

    def help_message_group(self, groupDisplayName="GROUP_NAME"):
        return f"Hello people of {groupDisplayName}!\n" \
               "Write these commands, so I can start your day off properly:\n" \
               "1. '!dog' : start your day with a cute random dog image\n" \
               "2. '!cat' : start your day with an adorable random cat image\n" \
               "3. '!help' : display this message again"

    def help_message_room(self, roomDisplayName="ROOM_NAME"):
        return f"Hello people of {roomDisplayName}!\n" \
               "Write these commands, so I can start your day off properly:\n" \
               "1. '!dog' : start your day with a cute random dog image\n" \
               "2. '!cat' : start your day with an adorable random cat image\n" \
               "3. '!help' : display this message again"



help_message_obj = HelpMessageUtil()
