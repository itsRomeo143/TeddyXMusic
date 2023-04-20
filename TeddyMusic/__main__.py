import asyncio
import importlib

from pytgcalls import idle

from TeddyMusic import BOT_USERNAME, bot, call_py
from TeddyMusic.Modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def TeddyX_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("TeddyMusic.Modules." + all_module)
    await bot.start()
    await call_py.start()
    await idle()
    print(f"ɢᴏᴏᴅʙʏᴇ!\nStopping @{BOT_USERNAME}")
    await bot.stop()


if __name__ == "__main__":
    loop.run_until_complete(TeddyX_boot())
