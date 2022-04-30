# @xmartperson

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from Rockz import app
from Rockz.core.call import Rock
from Rockz.utils.database import is_muted, mute_off
from Rockz.utils.decorators import AdminRightsCheck

# Commands
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")


@app.on_message(
    filters.command(UNMUTE_COMMAND) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_muted(chat_id):
        return await message.reply_text(_["admin_7"])
    await mute_off(chat_id)
    await Rock.unmute_stream(chat_id)
    await message.reply_text(
        _["admin_8"].format(message.from_user.mention)
    )