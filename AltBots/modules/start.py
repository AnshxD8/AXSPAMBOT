from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("⚡𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 🔥", data="help_back"),
        Button.url("⚡🥵  𝐎𝐖𝐍𝐄𝐑  🔥⚡", "https://t.me/Ansh_xD8")
    ],
    [
        Button.url("𝐂𝐇𝐀𝐍𝐍𝐄𝐋⚡ ", "https://t.me/Ansh_xDz"),
        Button.url("⚡💥 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 💥⚡  ", "https://t.me/THE_INDRAPRASTHA")
    ],
    [
        Button.url(" CLAN ", "https://t.me/TEAM_R2F")
        
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ANSH](https://t.me/Ansh_xD8)**\n\n"
        TEXT += f"» **ᴅᴇᴀᴅ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/33ed260fcfc79eb82838b.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
)
