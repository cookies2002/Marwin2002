import random
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from Devine import app as devine
from config import ADDLISTLOG_ID, REMOVELISTLOG_ID

@devine.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message: Message):
    chat = message.chat
    link = await devine.export_chat_invite_link(chat.id)
    for member in message.new_chat_members:
        if member.id == devine.id:
            count = await devine.get_chat_members_count(chat.id)
            adder = message.from_user
            adder_username = f"@{adder.username}" if adder and adder.username else "No username"
            adder_id = adder.id if adder else "Unknown ID"
            msg = (
                f"ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"ᴄʜᴀᴛ ɴᴀᴍᴇ: <code>{chat.title}</code>\n"
                f"ᴄʜᴀᴛ ɪᴅ: <code>{chat.id}</code>\n"
                f"ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{chat.username}\n"
                f"ᴄʜᴀᴛ ʟɪɴᴋ : {link}\n"
                f"ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs : {count}\n\n"
                f"ᴀᴅᴅᴇᴅ ʙʏ : {adder.mention}\n"
                f"ᴀᴅᴅᴇʀ ᴜsᴇʀɴᴀᴍᴇ: {adder_username}\n"
                f"ᴀᴅᴅᴇʀ ɪᴅ : <code>{adder_id}</code>"
            )
            await devine.send_message(ADDLISTLOG_ID, text=msg, parse_mode=ParseMode.HTML)

@devine.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await devine.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user
        remover_username = f"@{remove_by.username}" if remove_by and remove_by.username else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        remover_id = remove_by.id if remove_by else "Unknown ID"
        remover_mention = remove_by.mention if remove_by else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"

        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        chat_id = message.chat.id

        left_message = (
            f"<b>#Left_group</b>\n\n"
            f"ᴄʜᴀᴛ ᴛɪᴛʟᴇ : <code>{title}</code>\n"
            f"ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ : {username}\n"
            f"ᴄʜᴀᴛ ɪᴅ : <code>{chat_id}</code>\n\n"
            f"ʀᴇᴍᴏᴠᴇᴅ ʙʏ : {remover_mention}\n"
            f"ʀᴇᴍᴏᴠᴇʀ ᴜsᴇʀɴᴀᴍᴇ : {remover_username}\n"
            f"ʀᴇᴍᴏᴠᴇʀ ɪᴅ : <code>{remover_id}</code>"
        )
        await devine.send_message(REMOVELISTLOG_ID, text=left_message, parse_mode=ParseMode.HTML)
