import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


import logging
from aiogram import Bot, Dispatcher, executor, types
from environs import Env
import keyboards as kb
from mainapp.models import CityInfo


env = Env()
env.read_env()


logging.basicConfig(level=logging.INFO)
bot = Bot(token=env('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Здравствуйте, выберите город или введите имя города.", reply_markup=kb.start_kb)


@dp.message_handler()
async def echo(message: types.Message):
    sent_answer = False
    check_city = CityInfo.objects.filter(city_name__icontains=message.text)
    if check_city and check_city.count() != 1:
        await message.answer("Список найденных городов, выберите для подробности",
                             reply_markup=kb.get_city_by_name(check_city))
        sent_answer = True
    if check_city and check_city.count() == 1:
        check_city = check_city.first()
        await message.answer(f"Название города: {check_city.city_name}\n"
                             f"Количество населения: {check_city.population}\n"
                             f"Ссылка на wiki: {check_city.url}")
        sent_answer = True
    if not sent_answer:
        if message.text == "🌆 Города":
            await message.answer("Список всех городов, выберите для подробности",
                                 reply_markup=kb.get_all_cities_keyboard())
        else:
            await message.answer("Ничего не найдено")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
