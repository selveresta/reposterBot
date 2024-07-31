import asyncio

from aiogram import Bot
from aiogram.types import InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from threading import Thread


class MessagePost:
    groups = []
    text = ""
    url = ""
    url_text = ""
    photo = ""

    sentMessages = []

    thread = None
    markup = None
    sending = True

    def __init__(self, groups, text, url, url_text, photo="photo.jpg"):
        self.groups = groups
        self.text = text
        self.url = url
        self.url_text = url_text
        self.photo = FSInputFile(photo)

        self.create_markup()

    def create_markup(self):
        builder = InlineKeyboardBuilder()

        builder.add(InlineKeyboardButton(text=self.url_text, url=self.url))

        self.markup = builder.as_markup()

    async def create_and_start_task(self, bot: Bot):
        loop = asyncio.get_event_loop()

        def startup(loop):
            asyncio.run_coroutine_threadsafe(self.start_sendind(bot), loop)

        self.thread = Thread(target=startup, args=[loop])

        self.thread.start()

    async def start_sendind(self, bot: Bot):

        self.sending = True
        while True:
            if not self.sending:
                break

            for g in self.groups:
                try:
                    m = await bot.send_photo(
                        g,
                        photo=self.photo,
                        caption=self.text,
                        reply_markup=self.markup,
                    )
                    self.sentMessages.append({"m": m.message_id, "g": g})
                except Exception as e:
                    self.sending = False
                    print(e)
                    try:
                        await bot.delete_message(g, m.message_id)
                    except Exception as ex:
                        print(ex)
                        break

            await asyncio.sleep(120)

            for p in self.sentMessages:
                await bot.delete_message(p["g"], p["m"])
                self.sentMessages = []

    async def stop_sending(self, bot: Bot):
        self.sending = False

        for p in self.sentMessages:
            try:
                await bot.delete_message(p["g"], p["m"])
                self.sentMessages = []
            except Exception as e:
                print(e)
                continue
