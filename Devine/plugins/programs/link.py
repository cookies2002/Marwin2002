from pyrogram import filters 
from Devine import app
 
@app.on_message(filters.command("link"))
async def link_handler(client, message): 
    if len(message.command) < 2: 
        return await message.reply_text("ᴘʀᴏᴠɪᴅᴇ ᴀ ᴄʜᴀᴛ ɪᴅ ᴛᴏ ʀᴇᴛʀɪᴇᴠᴇ ɪᴛs ʟɪɴᴋ.") 
 
    target_chat_id = message.command[1] 
 
    try: 
        chat = await app.get_chat(int(target_chat_id)) 
        if chat.username: 
            chat_link = f"https://t.me/{chat.username}" 
        else: 
            chat_link = await app.export_chat_invite_link(int(target_chat_id)) 
 
        await message.reply_text(f"ʜᴇʀᴇ ɪs ᴛʜᴇ ᴄʜᴀᴛ ʟɪɴᴋ ғᴏʀ {chat.title}: {chat_link}") 
 
    except ChatAdminRequired: 
        return await message.reply_text("ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ ᴏʀ ɴᴏᴛ ᴛʜᴇʀᴇ.") 
    except Exception as e: 
        return await message.reply_text( 
            f"An error occurred: {type(e).name}. Please try again later." 
        )
