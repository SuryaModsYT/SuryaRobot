
from pyrogram import filters

from Tianabot.pyrogramee.pluginshelper import admins_only, get_text
from Tianabot import pbot


@pbot.on_message(
    filters.command("send") & ~filters.edited & ~filters.bot & ~filters.private
)
@admins_only
async def send(client, message):
    args = get_text(message)
    await client.send_message(message.chat.id, text=args)
