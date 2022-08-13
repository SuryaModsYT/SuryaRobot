from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client, dispatcher, OWNER_USERNAME


ANON = "https://telegra.ph/file/7bd111132fce009e4605e.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝗦𝗨𝗥𝗬𝗔](tg://user?id=5043850742)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**𝙎𝙪𝙧𝙮𝙖 𝙈𝙪𝙨𝙞𝙘 ✘ 𝙍𝙤𝙗𝙤𝙩 is not open sourced anymore.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                ],
       [  
        InlineKeyboardButton(text="💙 𝗖𝗵𝗮𝘁𝘁𝗶𝗻𝗴 𝗛𝘂𝗯 💙️", url=f"https://t.me/FRIENDS4EVERCHAT"),
    ], 
    
        [  
        InlineKeyboardButton(text="💫 𝙈𝙪𝙨𝙞𝙘 𝘽𝙤𝙩 𝙍𝙚𝙥𝙤 💫", url=f"https://github.com/SuryaModsYT/SuryaModsMusicBot"),
    ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
