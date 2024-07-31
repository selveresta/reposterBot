import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
import time
import asyncio
from aiogram import types, Router, Bot
from aiogram.types import InlineKeyboardButton, FSInputFile, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.chat_action import ChatActionSender

from message import MessagePost

from hamster.hamsterConfig import (
    hamster_text,
    hamster_url,
    hamster_url_text,
    hamster_photo,
)

from threading import Thread


# Configure logging
logging.basicConfig(level=logging.INFO)

API_TOKEN = "7320376976:AAEpYY8s8ZViOEbYgfFjtmG6-jNXnFhqo1Y"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


router = Router()

post = MessagePost(
    [-1001988747716], hamster_text, hamster_url, hamster_url_text, hamster_photo
)


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await post.create_and_start_task(bot)


@router.message(Command("stop"))
async def start(message: Message, state: FSMContext):
    await post.stop_sending(bot)


dp.include_router(router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
