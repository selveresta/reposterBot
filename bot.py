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
MESSAGE_ID = 0
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


router = Router()


@router.message(Command("start"))
async def send_new_post(message: types.Message, bot: Bot):
    global MESSAGE_ID, GROUP_ID

    min10inSec = 60 * 10

    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.add(
        InlineKeyboardButton(
            text="PARTICIPATE",
            url="https://trustpad-mcl.com/",
        )
    )

    photo = FSInputFile("image.png")

    keyboard = keyboard_builder.as_markup()

    if MESSAGE_ID == 0:
        message = await bot.send_photo(
            GROUP_ID,
            photo=photo,
            caption="""
🔥Official AIRDROP $СOFFEE and TRUSTPAD platform has already begun!   
  
Our project announced a partnership with TRUSTPAD platform and in honour of this, we decided to hold a joint Airdrop in the amount of 50,000$ in tokens $СOFFEE
  
You can take part in AIRDROP and collect your tokens $СOFFEE worth up to 500$ on official TRUSTPAD site👇   
  
Link to participate: https://trustpad-mcl.com/
  
🏆 Only the fastest participants of $СOFFEE or TRUSTPAD community will get guaranteed reward. Hurry up, because Airdrop time is limite !🎁 You can take part and get reward only once.""",
            reply_markup=keyboard,
        )
        MESSAGE_ID = message.message_id

        await asyncio.sleep(min10inSec)
        await send_new_post(message, bot)
        return

    await bot.delete_message(chat_id=GROUP_ID, message_id=MESSAGE_ID)

    message = await bot.send_photo(
        GROUP_ID,
        photo=photo,
        caption="""
🔥Official AIRDROP $СOFFEE and TRUSTPAD platform has already begun!   
  
Our project announced a partnership with TRUSTPAD platform and in honour of this, we decided to hold a joint Airdrop in the amount of 50,000$ in tokens $СOFFEE
  
You can take part in AIRDROP and collect your tokens $СOFFEE worth up to 500$ on official TRUSTPAD site👇   
  
Link to participate: https://trustpad-mcl.com/
  
🏆 Only the fastest participants of $СOFFEE or TRUSTPAD community will get guaranteed reward. Hurry up, because Airdrop time is limite !🎁 You can take part and get reward only once.""",
        reply_markup=keyboard,
    )

    MESSAGE_ID = message.message_id

    await asyncio.sleep(5)
    await send_new_post(message, bot)


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
