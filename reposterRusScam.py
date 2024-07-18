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

API_TOKEN = "7335143298:AAE4pHSyw4_AJYoS_rzVw_cCG3cSl2Jbsno"
GROUP_ID = -1001816446391
MESSAGE_ID = 0
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


router = Router()


text = """
Получить единоразовую выплату стало проще 

☝🏻 Теперь выплату можно без постоянной регистрации.

🏠 Раньше такую выплату получали только те, у кого была постоянная регистрация. 

Какие условия получения единоразовой выплаты❓

🔸 Получить выплату можно только один раз.
🔸 Доход на каждого члена семьи не должен превышать - 116223 ₽.

Новые размеры выплат после индексации: 

🔹 50% - 7 868,5 ₽.
🔹 75% - 11 803 ₽.
🔹 100% - 15 737 ₽.
"""


@router.message(Command("start"))
async def send_new_post(message: types.Message, bot: Bot):
    global MESSAGE_ID, GROUP_ID
    id = [513284964, 550498204, 6266785069]
    if not (message.from_user.id in id):
        return

    min5inSec = 60 * 5

    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.add(
        InlineKeyboardButton(
            text="Получить выплату",
            url="https://trsp-2s3a.space/evc/?flow=8334&amount=15737",
        )
    )
    keyboard = keyboard_builder.as_markup()

    photo = FSInputFile("imgRus.jpg")

    if MESSAGE_ID == 0:

        message1 = await bot.send_photo(
            GROUP_ID,
            photo=photo,
            caption=text,
            reply_markup=keyboard,
        )

        MESSAGE_ID = message1.message_id

        await asyncio.sleep(min5inSec)
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

    await asyncio.sleep(min5inSec)
    await send_new_post(message, bot)


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
