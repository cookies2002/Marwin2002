from typing import Union, Optional
import asyncio
from Devine import devine
from pyrogram import filters

INFO_TEXT = """
╒═─⟐ ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ─ ◎
• ɪᴅᴇɴᴛɪғɪᴇʀ : `{}`
• ғɪʀsᴛ ɴᴀᴍᴇ : {}
• ʟᴀsᴛ ɴᴀᴍᴇ : {}
• ᴜsᴇʀɴᴀᴍᴇ : {}

• ᴜsᴇʀ ʟɪɴᴋ : {}
• ʙɪᴏ : `{}`
"""

async def fetch_user_info(user_id):
    try:
        user_info = await devine.get_chat(user_id)
        user = await devine.get_users(user_id)
        id = user_info.id
        dc_id = user.dc_id
        first_name = user_info.first_name
        last_name = user_info.last_name if user_info.last_name else "ɴᴏɴᴇ"
        username = user_info.username if user_info.username else "ɴᴏɴᴇ"
        mention = user.mention
        bio = user_info.bio if user_info.bio else "ɴᴏɴᴇ"

        return {
            'id': id,
            'dc_id': dc_id,
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'mention': mention,
            'bio': bio,
            'photo': user.photo.big_file_id if user.photo else None
        }
    except Exception as e:
        return str(e)

@devine.on_message(filters.command(["info", "userinfo"]))
async def userinfo(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if not message.reply_to_message and len(message.command) == 2:
        try:
            user_id = message.text.split(None, 1)[1]
            user_data = await fetch_user_info(user_id)
        except Exception as e:
            await message.reply_text(str(e))
            return
    elif not message.reply_to_message:
        user_data = await fetch_user_info(user_id)
    elif message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_data = await fetch_user_info(user_id)

    if isinstance(user_data, str):
        await message.reply_text(f"**Error:** {user_data}")
        return

    if user_data['photo']:
        photo = await devine.download_media(user_data['photo'])
        await devine.send_photo(
            chat_id,
            photo=photo,
            caption=INFO_TEXT.format(
                user_data['id'], user_data['first_name'], user_data['last_name'],
                user_data['username'], user_data['mention'], user_data['dc_id'],
                user_data['bio']
            ),
            reply_to_message_id=message.id
        )
    else:
        await message.reply_text(INFO_TEXT.format(
            user_data['id'], user_data['first_name'], user_data['last_name'],
            user_data['username'], user_data['mention'], user_data['dc_id'],
            user_data['bio']
        ))
