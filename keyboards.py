import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


from aiogram import types
from mainapp.models import CityInfo


buttons = {
    'cities': types.KeyboardButton('🌆 Города')
}
start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(buttons['cities'])


def get_all_cities_keyboard():
    cities = CityInfo.objects.all()
    cities_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for city in cities:
        cities_kb.add(types.KeyboardButton(str(city.city_name)))
    return cities_kb


def get_city_by_name(city_obj):
    cities_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for city in city_obj:
        cities_kb.add(types.KeyboardButton(str(city.city_name)))
    return cities_kb
