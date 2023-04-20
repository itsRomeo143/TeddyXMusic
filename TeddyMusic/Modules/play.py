from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioImagePiped
from pytgcalls.types.input_stream.quality import MediumQualityVideo
from youtubesearchpython import VideosSearch

from TeddyX.filters import command, other_filters
from TeddyX.inline import audio_markup, stream_markup
from TeddyX.queues import QUEUE, add_to_queue
from TeddyX.thumbnail import play_thumb, queue_thumb
from TeddyX.utils import bash
from TeddyMusic import BOT_USERNAME
from TeddyMusic import Romeo as user
from TeddyMusic import bot as Romeo
from TeddyMusic import call_py
from TeddyMusic.config import IMG_1, IMG_2, IMG_5


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0


async def ytdl(format: str, link: str):
    stdout, stderr = await bash(
        f'yt-dlp --geo-bypass -g -f "[height<=?720][width<=?1280]" {link}'
    )
    if stdout:
        return 1, stdout.split("\n")[0]
    return 0, stderr


chat_id = None
DISABLED_GROUPS = []
useer = "NaN"
ACTV_CALLS = []


@Romeo.on_message(command(["play", f"play@{BOT_USERNAME}"]) & other_filters)
async def play(c: Romeo, m: Message):
    await m.delete()
    replied = m.reply_to_message
    chat_id = m.chat.id
    user_id = m.from_user.id
    buttons = audio_markup(user_id)
    if m.sender_chat:
        return await m.reply_text(
            "ʏᴏᴜ'ʀᴇ ᴀɴ __ᴀɴᴏɴʏᴍᴏᴜs__ ᴀᴅᴍɪɴ !\n\n» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs."
        )
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"Error:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 ᴛᴏ ᴜsᴇ ᴍᴇ, ɪ ɴᴇᴇᴅ ᴛᴏ ʙᴇ ᴀɴ **ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ** ᴡɪᴛʜ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ **ᴘᴇʀᴍɪssɪᴏɴs**:\n\n» ❌ __ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs__\n» ❌ __ᴀᴅᴅ ᴜsᴇʀs__\n» ❌ __ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ__\n\nᴅᴀᴛᴀ ɪs **ᴜᴘᴅᴀᴛᴇᴅ** ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀғᴛᴇʀ ʏᴏᴜ **ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ**"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "ᴍɪssɪɴɢ ʀᴇǫᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ:" + "\n\n» ❌ __ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("ᴍɪssɪɴɢ ʀᴇǫᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴ:" + "\n\n» ❌ __ɪɴᴠɪᴛᴇ ᴜsᴇʀ__")
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_USERNAME} **ɪs ʙᴀɴɴᴇᴅ ɪɴ ɢʀᴏᴜᴘ** {m.chat.title}\n\n» **ᴜɴʙᴀɴ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ғɪʀsᴛ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **ᴜsᴇʀʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ**\n\n**ʀᴇᴀsᴏɴ**: `{e}`")
                return
        else:
            try:
                invitelink = await c.export_chat_invite_link(m.chat.id)
                if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+", "https://t.me/joinchat/"
                    )
                await user.join_chat(invitelink)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **ᴜsᴇʀʙᴏᴛ ғᴀɪʟᴇᴅ ᴛᴏ ᴊᴏɪɴ**\n\n**ʀᴇᴀsᴏɴ**: `{e}`"
                )
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴀᴜᴅɪᴏ...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 **ᴛʀᴀᴄᴋ ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ »** `{pos}`\n\n🏷 **ɴᴀᴍᴇ:** [{songname}]({link}) | `ᴍᴜsɪᴄ`\n💭 **ᴄʜᴀᴛ:** `{chat_id}`\n🎧 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {m.from_user.mention()}",
                    reply_markup=InlineKeyboardMarkup(buttons),
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            dl,
                        ),
                        stream_type=StreamType().local_stream,
                    )
                    add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                    await suhu.delete()
                    requester = (
                        f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                    )
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        caption=f"🏷 **ɴᴀᴍᴇ:** [{songname}]({link})\n💭 **ᴄʜᴀᴛ:** `{chat_id}`\n💡 **sᴛᴀᴛᴜs:** `ᴘʟᴀʏɪɴɢ`\n🎧 **ʀᴇǫᴜᴇsᴛ ʙʏ:** {requester}\n📹 **sᴛʀᴇᴀᴍ ᴛʏᴘᴇ:** `ᴍᴜsɪᴄ`",
                        reply_markup=InlineKeyboardMarkup(buttons),
                    )
                except Exception as e:
                    await suhu.delete()
                    await m.reply_text(f"🚫 ᴇʀʀᴏʀ:\n\n» {e}")

    else:
        if len(m.command) < 2:
            await m.reply_photo(
                photo=f"{IMG_5}",
                caption="**ᴜsᴀɢᴇ: /play ɢɪᴠᴇ ᴀ ᴛɪᴛʟᴇ sᴏɴɢ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/RomeoSupport"
                            ),
                            InlineKeyboardButton("• ᴄʟᴏsᴇ", callback_data="cls"),
                        ]
                    ]
                ),
            )
        else:
            suhu = await m.reply_text(f"**Teddy ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ**\n\n100% ▓▓▓▓▓▓▓▓▓▓▓▓ 00%")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("💬 **ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ.**")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = m.from_user.id
                gcname = m.chat.title
                videoid = search[4]
                dlurl = f"https://www.youtubepp.com/watch?v={videoid}"
                info = f"https://t.me/TeddyMusicBot?start=info_{videoid}"
                keyboard = stream_markup(user_id, dlurl)
                playimg = await play_thumb(videoid)
                queueimg = await queue_thumb(videoid)
                await suhu.edit(
                    f"**ɴɪʙɪ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ**\n\n**ᴛɪᴛʟᴇ**: {title[:22]}\n\n100% ▓▓▓▓▓▓▓▓▓▓▓▓0%\n\n**ᴛɪᴍᴇ ᴛᴀᴋᴇɴ**: 00:00 sᴇᴄᴏɴᴅs\n\n**ᴄᴏɴᴠᴇʀᴛɪɴɢ ᴀᴜᴅɪᴏ[ғғᴍᴘᴇɢ ᴘʀᴏᴄᴇss]**"
                )
                format = "bestaudio"
                abhi, ytlink = await ytdl(format, url)
                if abhi == 0:
                    await suhu.edit(f"💬 yt-dl ɪssᴜᴇs ᴅᴇᴛᴇᴄᴛᴇᴅ\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=queueimg,
                            caption=f"⏳ ᴀᴅᴅᴇᴅ ᴛᴏ ǫᴜᴇᴜᴇ ᴀᴛ {pos}\n\n👤ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:{requester}\nɪɴғᴏʀᴍᴀᴛɪᴏɴ [ʜᴇʀᴇ]({info})",
                            reply_markup=InlineKeyboardMarkup(keyboard),
                        )
                    else:
                        try:
                            await suhu.edit(
                                f"**Teddy ᴅᴏᴡɴʟᴏᴀᴅᴇʀ**\n\n**ᴛɪᴛʟᴇ**: {title[:22]}\n\n0% ████████████100%\n\n**ᴛɪᴍᴇ ᴛᴀᴋᴇɴ**: 00:00 sᴇᴄᴏɴᴅs\n\n**ᴄᴏɴᴠᴇʀᴛɪɴɢ ᴀᴜᴅɪᴏ[ғғᴍᴘᴇɢ ᴘʀᴏᴄᴇss]**"
                            )
                            await call_py.join_group_call(
                                chat_id,
                                AudioImagePiped(
                                    ytlink,
                                    playimg,
                                    video_parameters=MediumQualityVideo(),
                                ),
                                stream_type=StreamType().local_stream,
                            )

                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)

                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=playimg,
                                caption=f"📡 sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ ᴀᴜᴅɪᴏ 💡\n\n👤ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ:{requester}\nɪɴғᴏʀᴍᴀᴛɪᴏɴ [ʜᴇʀᴇ]({info})",
                                reply_markup=InlineKeyboardMarkup(keyboard),
                            )
                        except Exception as ep:
                            await suhu.delete()
                            await m.reply_text(f"💬 ᴇʀʀᴏʀ: `{ep}`")
