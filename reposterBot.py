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

API_TOKEN = ""
GROUP_ID = -1001792317500
GROUP_ID_TWO = -1001813741487
GROUP_ID_THREE = -1001820466879
MESSAGE_ID = 0
MESSAGE_ID_TWO = 0
MESSAGE_ID_THREE = 0
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


router = Router()


text = """
❗️Hamster Combat announces AIRDROP❗️

Join the HamsterCombat airdrop and win your share of $500 in HMSTR tokens! 
🎉 Participate easily through our airdrop bot and claim your rewards. This airdrop is FCFS (First Come, First Served) for the first 50,000 participants. 🚀

#HamsterCombat #Airdrop #HMSTR #CryptoGiveaway #Milestone #ThankYou #OnwardAndUpward #crypto #btc #memetoken #memecoin #hamster #taptap #clicker #game #p2e
"""


text1 = """
❗️Announced AIRDROP Hamster Kombat ❗️ 

🎉 Join the Hamster Kombat airdrop and win your share of $500 in HMSTR tokens!  🎉
This airdrop is FCFS (First Come, First Served) for the first 50,000 participants.  🚀

#HamsterCombat #Airdrop #HMSTR #CryptoGiveaway #Milestone #ThankYou #OnwardAndUpward #crypto #btc #memetoken #memecoin #hamster #taptap #clicker #game #p2e
"""


@router.message(Command("start"))
async def send_new_post(message: types.Message, bot: Bot):
    global MESSAGE_ID, GROUP_ID, GROUP_ID_TWO, MESSAGE_ID_TWO, GROUP_ID_THREE, MESSAGE_ID_THREE

    min10inSec = 60 * 10

    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.add(
        InlineKeyboardButton(
            text="CLAIM",
            url="https://hamsters-kombats.site/",
        )
    )
    keyboard = keyboard_builder.as_markup()

    keyboard_builder1 = InlineKeyboardBuilder()
    keyboard_builder1.add(
        InlineKeyboardButton(
            text="CLAIM",
            url="https://hamster-combats.site",
        )
    )
    keyboard1 = keyboard_builder1.as_markup()

    photo = FSInputFile("image.jpg")
    photo1 = FSInputFile("image1.jpg")

    if MESSAGE_ID_TWO == 0 and MESSAGE_ID_THREE == 0 and MESSAGE_ID:

        message1 = await bot.send_photo(
            GROUP_ID,
            photo=photo,
            caption=text,
            reply_markup=keyboard,
        )

        message2 = await bot.send_photo(
            GROUP_ID_TWO,
            photo=photo,
            caption=text,
            reply_markup=keyboard,
        )

        message3 = await bot.send_photo(
            GROUP_ID_THREE,
            photo=photo1,
            caption=text1,
            reply_markup=keyboard1,
        )

        MESSAGE_ID = message1.message_id
        MESSAGE_ID_TWO = message2.message_id
        MESSAGE_ID_THREE = message3.message_id

        await asyncio.sleep(min10inSec)
        await send_new_post(message, bot)
        return

    await bot.delete_message(chat_id=GROUP_ID, message_id=MESSAGE_ID)
    await bot.delete_message(chat_id=GROUP_ID_TWO, message_id=MESSAGE_ID_TWO)
    await bot.delete_message(chat_id=GROUP_ID_THREE, message_id=MESSAGE_ID_THREE)

    message1 = await bot.send_photo(
        GROUP_ID_TWO,
        photo=photo,
        caption=text,
        reply_markup=keyboard,
    )

    message2 = await bot.send_photo(
        GROUP_ID_TWO,
        photo=photo,
        caption=text,
        reply_markup=keyboard,
    )

    message3 = await bot.send_photo(
        GROUP_ID_THREE,
        photo=photo1,
        caption=text1,
        reply_markup=keyboard1,
    )

    MESSAGE_ID = message1.message_id
    MESSAGE_ID_TWO = message2.message_id
    MESSAGE_ID_THREE = message3.message_id

    await asyncio.sleep(min10inSec)
    await send_new_post(message, bot)


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
