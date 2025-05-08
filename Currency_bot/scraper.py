import datetime
import sqlite3
import time

import requests
from bs4 import BeautifulSoup

url_dollar = 'https://www.tgju.org/profile/price_dollar_rl'

urls = {
    'دلار': 'https://www.tgju.org/profile/price_dollar_rl',
    'دلار کانادا': 'https://www.tgju.org/profile/price_dollar_rl',
    'یورو': 'https://www.tgju.org/profile/price_eur',
    'پوند انگلیس': 'https://www.tgju.org/profile/price_gbp',
    'دینار عراق': 'https://www.tgju.org/profile/price_iqd',
    'طلا 18 عیار': 'https://www.tgju.org/profile/geram18',
    'طلا 24 عیار': 'https://www.tgju.org/profile/geram24',
    'مثقال طلا': 'https://www.tgju.org/profile/mesghal',
    'سکه امامی': 'https://www.tgju.org/profile/sekee',
    'سکه بهار آزادی': 'https://www.tgju.org/profile/sekeb',

}


def get_dollar_price():
    response = requests.get(urls['دلار'])

    if response.status_code != 200:
        return "خطا در دریافت اطلاعات ❌"

    soup = BeautifulSoup(response.text, 'html.parser')

    price_tag = soup.find('span[data-col="info.last_trade.PDrCotVal"]')

    if price_tag:
        return f"💵 قیمت دلار: {price_tag.text.strip()} تومان"
    else:
        return "قیمت پیدا نشد ❌"


def get_price(url):
    response = requests.get(url)
    # print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser') if response.status_code == 200 else None
    price_tag = soup.find('span', class_='value')
    # print(type(price_tag.text.strip()))
    # if price_tag:
    #     price = price_tag.text.strip().split('\n')
    #     return price
    # else:
    #     return "❌ قیمت پیدا نشد"

    return price_tag.text.strip().split("\n")[0] if price_tag else "❌ قیمت پیدا نشد"
    # for name, price in price_tag:
    #     print(name, price)


def get_all_prices():
    prices = {name: get_price(url) for name, url in urls.items()}
    return prices


def get_dates_prices():
    response = requests.get(urls['دلار'])

    # if response.status_code !=200:
    #     return "خطا در دریافت اطلاعات ❌"
    soup = BeautifulSoup(response.text, 'html.parser') if response.status_code == 200 else None


def get_last_5_days_prices():
    url = 'https://www.tgju.org/profile/geram18/history'

    try:
        response = requests.get(url)
        table = BeautifulSoup(response.text, 'html.parser') if response.status_code == 200 else None  # پیدا کردن جدول
        rows = table.find('table').find_all('tr', limit=6)  # گرفتن 6 سطر آخر

        prices = {}

        for row in rows:
            columns = row.find_all('td')

            if len(columns) < 4:  # بررسی اینکه حداقل ۴ ستون داشته باشد
                continue

            final_price = columns[3].text.strip().replace(',', '')
            date = columns[-1].text.strip()

            try:
                prices[date] = int(final_price)
            except ValueError:
                continue
        return prices
    except requests.exceptions.RequestException as e:
        print(f"❌ خطا در دریافت داده‌ها: {e}")
        return {}


pricess = get_last_5_days_prices()
print(pricess)


def save_prices_to_database():
    prices = get_all_prices()
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()

    for name, price in prices.items():
        old_prices , old_timestamp = get_last_price(name)
        if str(price) != str(old_prices):
        # print(price)
        # print(cached_prices)
        # if str(price) != str(cached_prices)
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            timestamp = old_timestamp


        cursor.execute('''
            INSERT INTO prices(name,price,last_update)
            VALUES (?,?,?)
            ON CONFLICT (name) DO UPDATE SET 
            price = EXCLUDED.price,
            last_update = EXCLUDED.last_update
        
        ''', (name, price, timestamp))

        conn.commit()
    conn.close()

def get_last_price(name):
    conn = sqlite3.connect('prices.db')
    cursor = conn.cursor()

    cursor.execute('SELECT price , last_update FROM prices WHERE name = ?',(name,))
    result = cursor.fetchone()

    conn.close()
    return result if result else (None, None)
# def update_prices_periodically():
#     price_update =
#     while True:
#         prices = get_all_prices()
#         save_prices_to_database(prices)
#         print(f'prices updated at {datetime.now()}')
#         time.sleep(1800)


if __name__ == "__main__":
    print(get_all_prices())
    # for name,price in pricess.items():
    #     print(get_last_price(name))
    # print(save_prices_to_database(pricess))
    # update_prices_periodically()
    # print(get_dates_prices())
