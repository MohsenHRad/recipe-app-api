from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import CommandHandler, Application, CallbackContext, CallbackQueryHandler

from chart import draw_price_chart
from scraper import get_all_prices, get_last_5_days_prices

# python-telegram-bot → برای ساخت و مدیریت ربات تلگرام
# requests → برای گرفتن اطلاعات قیمت از API
# matplotlib → برای رسم نمودار تغییرات قیمت
TOKEN = '7981755421:AAEF1r1EjZqJXLaTMasZEyAVVFNe1FfXRw8'


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("سلام! من ربات قیمت ارز و طلا هستم. 🤖")


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
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("لطفاً دسته‌بندی مورد نظر را انتخاب کنید:", reply_markup=reply_markup)


async def button_clicked(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    prices = get_all_prices()

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
            await draw_chart_command(context.bot.token,query.message.chat.id)
    else:
        await query.message.reply_text("❌ خطا در دریافت داده‌ها برای نمودار.")
        # filtered_price = prices

    message = "\n___________________________\n".join(
        f"{name} : {price} ریال " for name, price in filtered_price.items())
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


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('prices', prices_command))
    app.add_handler(CallbackQueryHandler(button_clicked))
    print("ربات راه‌اندازی شد... 🚀")
    app.run_polling()


if __name__ == '__main__':
    main()
