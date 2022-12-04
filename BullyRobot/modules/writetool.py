import requests
from requests import get
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from BullyRobot import pbot as fallen, BOT_NAME, BOT_USERNAME


@fallen.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await fallen.send_message(
            message.chat.id, "`ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...,\n\nɪ ᴀᴍ ᴡʀɪᴛɪɴɢ ʏᴏᴜʀ ᴛᴇxᴛ...`"
        )
        API = f"https://api.sdbots.tk/write?text={text}"
        req = requests.get(API).url
        caption = f"""
ᴛᴇxᴛ ɪs ᴡʀɪᴛᴛᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ 💘
✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
❄ **ᴍᴏɴᴏ ʟɪɴᴋ :** `{req}`
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{req}")]]
            ),
        )
    else:
        lol = message.reply_to_message.text
        m = await fallen.send_message(
            message.chat.id, "`Please wait...,\n\nWriting your text...`"
        )
        API = f"https://api.sdbots.tk/write?text={lol}"
        req = requests.get(API).url
        caption = f"""
ᴛᴇxᴛ ɪs ᴡʀɪᴛᴛᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ 💘
✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
❄ **ᴍᴏɴᴏ ʟɪɴᴋ :** `{req}`
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=req,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{req}")]]
            ),
        )


__mod_name__ = "WʀɪᴛᴇTᴏᴏʟ✍️"

__help__ = """
 Wʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊
❍ /write <text> *:* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
 """

