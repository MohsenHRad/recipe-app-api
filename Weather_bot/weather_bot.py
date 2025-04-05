from datetime import datetime

import requests
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext, Application

Token = '7707616649:AAHyl4EndKhQefnPpU08MXTUOvgfGt79rW0'
API_KEY = '2529d04b6fb95326bc5ef1562ccb1490'
GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_closest_city(city: str):
    params = {
        'q': city,
        'limit': 5,
        'appid': API_KEY,
        'country': 'IR',

    }
    response = requests.get(GEOCODING_URL, params=params)
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return data.get('name'), data.get('lat'), data.get('lon')
    return None, None, None


def get_weather(city: str):
    city_close_name, lat, lon = get_closest_city(city)
    if not city_close_name:
        return 'نام شهر پیدا نشد یا خیلی نادر است ❗'

    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fa',


    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        tmp_min = data['main']['temp_min']
        tmp_max = data['main']['temp_max']
        pressure = data['main']['pressure']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
        return f'نام شهر : {city_name}\n' \
               f'دمای هوا : {temp} ℃ \n' \
               f' وضعیت هوا :{weather}\n' \
               f' محسوس :{feels_like} ℃\n' \
               f' رطوبت :{humidity}\n' \
               f' کمینه :{tmp_min} ℃\n ' \
               f' بیشینه :{tmp_max} ℃\n ' \
               f' فشار هوا :{pressure}\n' \
               f' طلوع آفتاب : {sunrise}\n' \
               f' غروب آفتاب : {sunset}\n'
    else:
        return "شهر پیدا نشد یا مشکلی در دریافت اطلاعات پیش اومد!"


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("سلام! من ربات آب‌وهوای تو هستم. دستور /help رو بزن تا راهنمایی بدم!")


async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("برای دریافت اطلاعات آب‌وهوا، شهر خودت رو وارد کن!")


async def handler_message(update: Update, context: CallbackContext) -> None:
    city = update.message.text
    weather_info = get_weather(city)
    await update.message.reply_text(weather_info)


def main():
    app = Application.builder().token(Token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler_message))

    print("ربات راه‌اندازی شد... 🚀")
    return app.run_polling()


if __name__ == "__main__":
    main()
