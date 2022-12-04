from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from BullyRobot import pbot as client


ANON = "https://telegra.ph/file/68c04e8ae8a76152eb5c0.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ ᴅᴇᴀʀ {message.from_user.mention()},\nɪ ᴀᴍ [ʙᴜʟʟʏ ✘ ʀᴏʙᴏᴛ-🇮🇩](t.me/bullyxguardianbot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝗕𝗨𝗟𝗟𝗬](https://t.me/jehrilla_cockroach)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

➻ ʙᴜʟʟʏ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪs ᴩʀɪᴠᴀᴛᴇ ɪᴛ ᴡɪʟʟ ʙᴇ ᴘᴜʙʟɪᴄ sᴏᴏɴ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url="https://t.me/jehrilla_cockroach"), 
                    InlineKeyboardButton(
                        "• sᴜᴘᴘᴏʀᴛ •", url="https://t.me/BullyxSupport")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
