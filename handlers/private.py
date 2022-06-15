import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/85f3e593108d2c4351f57.jpg",
        caption=f"""**𝐓𝐇𝐄 𝐁𝐄𝐒𝐓 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 𝐏𝐋𝐀𝐘𝐄𝐃 𝐈𝐍 𝐕𝐎𝐈𝐂𝐄 𝐂𝐇𝐀𝐓𝐒 𝐎𝐅 𝐆𝐑𝐎𝐔𝐏 , 𝐌𝐀𝐃𝐄 𝐖𝐈𝐓𝐇 𝐋𝐎𝐕𝐄 𝐀𝐍𝐃 𝐇𝐀𝐑𝐃𝐖𝐎𝐑𝐊 𝐁𝐘 [𝐀𝐆𝐎𝐑𝐀 𝐑𝐎𝐁𝐎𝐓𝐒](https://t.me/mr_agora)

𝐂𝐑𝐄𝐀𝐓𝐎𝐑 :- [𝐀𝐘𝐔𝐒𝐇](https://t.me/venom_kings)
𝐒𝐔𝐏𝐏𝐎𝐑𝐓:- [𝐖𝐎𝐑𝐋𝐃](https://t.me/venom_world_op)
𝐁𝐎𝐓𝐒 𝐒𝐄𝐑𝐕𝐄𝐑 :- [𝐀𝐆𝐎𝐑𝐀 𝐁𝐎𝐓𝐒](https://t.me/agora_robots)

 𝐅𝐈𝐑𝐒𝐓 𝐉𝐎𝐈𝐍 𝐓𝐇𝐈𝐒 [𝐒𝐄𝐑𝐕𝐄𝐑](t.me/team_agora) 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐄 𝐁𝐎𝐓 𝐀𝐍𝐃 𝐇𝐄𝐑𝐄 𝐈𝐒 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 𝐎𝐅 [𝐎𝐖𝐍𝐄𝐑](https://t.me/venom_kings)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💖 𝐎𝐖𝐍𝐄𝐑 💫", url=f"https://t.me/venom_world_op")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/85f3e593108d2c4351f57.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐑𝐄𝐏𝐎", url=f"https://github.com/MR-AGORA")
                ]
            ]
        ),
    )
