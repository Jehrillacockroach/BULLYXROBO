from telethon import events, Button, custom, version
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
import os,re
import requests
import datetime
import time
from datetime import datetime
import random
from PIL import Image
from io import BytesIO
from BullyRobot import telethn as bot
from BullyRobot import telethn as tgbot
from BullyRobot.events import register
from BullyRobot import dispatcher


edit_time = 5
""" =======================FALLEN ROBOT====================== """
file1 = "https://te.legra.ph/file/fd5f61591618f80fb44df.jpg"
file2 = "https://te.legra.ph/file/fd5f61591618f80fb44df.jpg"
file3 = "https://te.legra.ph/file/fd5f61591618f80fb44df.jpg"
file4 = "https://te.legra.ph/file/fd5f61591618f80fb44df.jpg"
file5 = "https://te.legra.ph/file/fd5f61591618f80fb44df.jpg"
""" =======================FALLEN ROBOT====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    chat = await event.get_chat()
    current_time = datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information",data="informations")]]
    on = await bot.send_file(event.chat_id, file=file2,caption= f"Hey {firstname}, \n Click on the button below \n to get info about you", buttons=button)

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button) 

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    LILIE = "ᴘᴏᴡᴇʀᴇᴅ ʙʏ 𝗕𝗨𝗟𝗟𝗬 \n\n"
    LILIE += f"ғɪʀsᴛ ɴᴀᴍᴇ : {PRO.first_name} \n"
    LILIE += f"ʟᴀsᴛ ɴᴀᴍᴇ : {PRO.last_name}\n"
    LILIE += f"ʏᴏᴜ ʙᴏᴛ : {PRO.bot} \n"
    LILIE += f"ʀᴇsᴛʀɪᴄᴛᴇᴅ : {PRO.restricted} \n"
    LILIE += f"ᴜsᴇʀ ɪᴅ : {boy}\n"
    LILIE += f"ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
    await event.answer(LILIE, alert=True)
  except Exception as e:
    await event.reply(f"{e}")


__command_list__ = [
    "myinfo"
]
