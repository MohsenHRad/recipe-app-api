import jdatetime
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt


def draw_price_chart(dates, prices, title='Price change chart'):
    dates = [jdatetime.datetime.strptime(date, '%Y/%m/%d').strftime('%Y/%m/%d') for date in dates]

    font_path = "fonts/Vazir-Medium.ttf"
    font_properties = fm.FontProperties(fname=font_path) if font_path else None

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # روزها را یکی یکی نمایش بده

    plt.figure(figsize=(18, 10))
    plt.xticks(rotation=45, font_properties=font_properties)
    plt.plot(dates, prices, marker='o', linestyle='-', color='b', label=title)
    plt.xlabel('Date', font_properties=font_properties,fontsize=15,loc='right')
    plt.ylabel('Price (Rial)', font_properties=font_properties,fontsize=15)
    plt.title(title, font_properties=font_properties,fontsize=15,loc='right')
    plt.legend(prop=font_properties)
    plt.grid()
    plt.savefig('chart.png')
    plt.close()
