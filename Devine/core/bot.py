from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class devine(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot...")
        super().__init__(
            name="Devine",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<b>{self.mention} ɪs ᴀʟɪᴠᴇ <a href='https://envs.sh/5Ci.jpg' target='_blank'>✨</a></b>\n\n"
                         f"<b>• ʙᴏᴛ ᴠᴇʀsɪᴏɴ :</b> <code>𝟸.𝟷 ʀx</code>\n"
                         f"<b>• ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :</b> <code>𝟹.𝟷𝟶.𝟷𝟷</code>\n"
                         f"<b>• ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :</b> <code>𝟸.𝟶.𝟷𝟶𝟼</code>"
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote your bot as an admin in your log group/channel."
            )
        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()

