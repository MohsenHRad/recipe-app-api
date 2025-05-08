import sqlite3

import asyncio
import nest_asyncio
nest_asyncio.apply()
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import CommandHandler, Application, CallbackContext, CallbackQueryHandler

from chart import draw_price_chart
from scraper import get_all_prices, get_last_5_days_prices, save_prices_to_database

# python-telegram-bot → برای ساخت و مدیریت ربات تلگرام
# requests → برای گرفتن اطلاعات قیمت از API
# matplotlib → برای رسم نمودار تغییرات قیمت
TOKEN = '7981755421:AAEF1r1EjZqJXLaTMasZEyAVVFNe1FfXRw8'


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("سلام! من ربات قیمت ارز و طلا هستم. 🤖")
    await update.message.reply_text('/help - برای راهنمایی را ارسال کنید')


async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('/start -  شروع دستورات\n' \
                                    '/help - راهنما\n'
                                    '/prices - قیمت ها '
                                    )


async def prices_command(update: Update, context: CallbackContext):
    # prices = get_all_prices()
    # for name, price in prices.items():
    #     await update.message.reply_text(f'{name} : {price} ریال')

    keyboard = [
        [InlineKeyboardButton("💰 ارز", callback_data='currency')],
        [InlineKeyboardButton("🪙 طلا", callback_data='gold')],
        [InlineKeyboardButton("📊 همه", callback_data='all')],
        [InlineKeyboardButton("📈 نمودار تغییرات", callback_data='chart')],
        # [InlineKeyboardButton("⌛ آخرین تغیرات ", callback_data='last_update')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("لطفاً دسته‌بندی مورد نظر را انتخاب کنید:", reply_markup=reply_markup)


async def button_clicked(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    prices = get_all_prices()
    save_prices_to_database()
    time_updated = get_last_updates()
    dict_time_updated = {name: time for name, _, time in time_updated}
    # print(time_updated)

    choice = query.data

    if choice == 'currency':
        filtered_price = {key: value for key, value in prices.items() if
                          key in ["یورو", "پوند انگلیس", "دلار", "دلار کانادا"]}

    elif choice == 'gold':
        filtered_price = {key: value for key, value in prices.items() if key in ["طلا 18 عیار",
                                                                                 "طلا 24 عیار",
                                                                                 "مثقال طلا",
                                                                                 "سکه امامی",
                                                                                 "سکه بهار آزادی"
                                                                                 ]}
    elif choice == 'chart':
        last_5_prices = get_last_5_days_prices()
        if last_5_prices:
            draw_price_chart(list(last_5_prices.keys()), list(last_5_prices.values()))
            await draw_chart_command(context.bot.token, query.message.chat.id)
    else:
        await query.message.reply_text("❌ خطا در دریافت داده‌ها برای نمودار.")
        return
        # filtered_price = prices
    message = message = "\n___________________________________________________________\n".join(
        f"{name} : {price} ریال\n⏰ آخرین بروزرسانی: {dict_time_updated.get(name, 'نامشخص')}"
        for name, price in filtered_price.items()
    )
    await update.callback_query.message.reply_text(message)


async def chart_command(update: Update, context: CallbackContext) -> None:
    prices_data = get_all_prices()

    dates = list(prices_data.keys()[-7:])
    prices = list(prices_data.values()[-7:])

    #
    # prices_date = get_last_5_days_prices()
    # if prices_date:
    #     draw_price_chart(list(prices_date.keys()), list(prices_date.values()))


async def draw_chart_command(bot_token, chat_id):
    bot = Bot(token=bot_token)
    with open('chart.png', 'rb') as photo:
        await bot.send_photo(chat_id=chat_id, photo=photo, caption="📊 نمودار تغییرات قیمت")


def get_last_updates():
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, price , last_update FROM prices')
    prices = cursor.fetchall()
    conn.close()

    return prices


def start_schdule():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(get_all_prices, 'interval', minutes=30)
    scheduler.start()
    return scheduler


async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('prices', prices_command))
    app.add_handler(CallbackQueryHandler(button_clicked))


    # scheduler = AsyncIOScheduler()
    # scheduler.add_job(get_all_prices, 'interval', minutes=4)
    # scheduler.start()
    start_schdule()


    print("ربات راه‌اندازی شد... 🚀")
    await app.run_polling(close_loop=False)


if __name__ == '__main__':
    # print(get_last_updates())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
