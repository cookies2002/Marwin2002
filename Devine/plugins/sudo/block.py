from pyrogram import filters
from pyrogram.types import Message

from Devine import app
from Devine.misc import SUDOERS
from Devine.utils.database import add_gban_user, remove_gban_user
from Devine.utils.decorators.language import language
from Devine.utils.extraction import extract_user
from config import filter


@app.on_message(filters.command(["block"]) & SUDOERS)
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in filter:
        return await message.reply_text(_["block_1"].format(user.mention))
    await add_gban_user(user.id)
    filter.add(user.id)
    await message.reply_text(_["block_2"].format(user.mention))


@app.on_message(filters.command(["unblock"]) & SUDOERS)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in filter:
        return await message.reply_text(_["block_3"].format(user.mention))
    await remove_gban_user(user.id)
    filter.remove(user.id)
    await message.reply_text(_["block_4"].format(user.mention))


@app.on_message(filters.command(["blocked", "blockedusers", "blusers"]) & SUDOERS)
@language
async def sudoers_list(client, message: Message, _):
    if not filter:
        return await message.reply_text(_["block_5"])
    mystic = await message.reply_text(_["block_6"])
    msg = _["block_7"]
    count = 0
    for users in filter:
        try:
            user = await app.get_users(users)
            user = user.first_name if not user.mention else user.mention
            count += 1
        except:
            continue
        msg += f"{count}➤ {user}\n"
    if count == 0:
        return await mystic.edit_text(_["block_5"])
    else:
        return await mystic.edit_text(msg)
