import random
import asyncio
from pyrogram import filters, __version__ as pver
from sys import version_info
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telethon import __version__ as tver
from telegram import __version__ as lver
from BullyRobot import BOT_USERNAME, OWNER_USERNAME, SUPPORT_CHAT, pbot

PHOTO = [
    "https://te.legra.ph/file/fd5f61591618f80fb44df.jpg",
    "https://te.legra.ph/file/fd5f61591618f80fb44df.jpg",
]

BULLY = [
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ", url=f"https://t.me/bullyxguardianbot?start=help"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/BullyxSupport"),
    ],
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/bullyxguardianbot?startgroup=true"),
    ],
]

@pbot.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ʙᴏᴏᴛɪɴɢ ᴜᴘ..")
    await asyncio.sleep(0.6)
    await accha.edit("ʙᴏᴏᴛᴇᴅ sᴜᴄᴄᴇsғᴜʟʟʏ...")
    await accha.delete()
    await asyncio.sleep(0.4)
    await m.reply_photo(
        random.choice(PHOTO),
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ ʙᴜʟʟʏ ᴍᴀɢᴜɪʀᴇ ʙᴏᴛ**
        ━━━━━━━━━━━━━━━━━━━
  » **ᴍʏ ʟᴏʀᴅ :** [𝗕𝗨𝗟𝗟𝗬](https://t.me/jehrilla_cockroach)
  » **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
  » **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
  » **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
  » **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
        ━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(BULLY)
    )
